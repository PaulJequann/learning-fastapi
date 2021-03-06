from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.models import models
# from db.database import engine
from app.routers import post, user, auth, vote


# models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Ya boy built an api. Hello world."}
