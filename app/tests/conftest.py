from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.oauth2 import create_access_token
from app.main import app
from app.core.config import settings
from app.db.database import get_db, Base
from app.models import models


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}_test"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="module")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()      
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture(scope="module")
def test_user(client):
    user_data ={
        "email": "testuser@gmail.com",
        "password": "password123"
    }
    response = client.post("/users/", json=user_data)

    assert response.status_code == 201
    new_user = response.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user["id"]})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client

@pytest.fixture
def test_posts(test_user, session):
    posts_data = [{
        "title": "first title",
        "content": "first content",
        "owner_id": test_user["id"]
    },{
        "title": "2nd title",
        "content": "2nd content",
        "owner_id": test_user["id"]
    },{
        "title": "3rd title",
        "content": "3rd content",
        "owner_id": test_user["id"]
    }]

    def create_post_model(post):
        return models.Post(**post)

    posts = list(map(create_post_model, posts_data))
    session.add_all(posts)
    session.commit()

    all_posts = session.query(models.Post).all()
    return all_posts