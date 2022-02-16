from app.schemas import schemas
def test_get_all_posts(authorized_client, test_posts):
    response = authorized_client.get("/posts")
    def validate(post):
        return schemas.PostOut(**post)
    posts_map = list(map(validate, response.json()))

    assert len(response.json()) == len(test_posts)
    assert response.status_code == 200

def test_unauthorized_user_get_all_posts(client, test_posts):
    response = client.get("/posts")
    assert response.status_code == 200

# def test_unauthorized_user_get_one_posts(client, test_posts):
#     response = client.get(f"/posts/{test_posts[0].id}")
#     assert response.status_code == 401

# def test_get_one_post_not_exist(authorized_client, test_posts):
#     response = authorized_client.get(f"/posts/888888")
#     assert response.status_code == 404