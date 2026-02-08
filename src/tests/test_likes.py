from fastapi import status
from core.settings import Settings
from constants import LIKE_RATING_HIGH, LIKE_RATING_AVG, film_uuid, user_uuid

settings = Settings()

def test_create_like(auth_client):
    response = auth_client.post(f"/api/v1/like/", json={
    "film_id": film_uuid,
    "like_value": LIKE_RATING_HIGH
})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json().get("like_value") == LIKE_RATING_HIGH
    assert response.json().get("user_id") == user_uuid
    assert response.json().get("film_id") == film_uuid

    response = auth_client.post(f"/api/v1/like/", json={
        "film_id": film_uuid,
        "like_value": LIKE_RATING_HIGH
    })
    assert response.status_code == status.HTTP_409_CONFLICT

def test_get_like(auth_client):
    response = auth_client.get(f"/api/v1/like/{film_uuid}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("like_value") == LIKE_RATING_HIGH
    assert response.json().get("user_id") == user_uuid
    assert response.json().get("film_id") == film_uuid

def test_patch_and_get_like(auth_client):
    response = auth_client.patch(f"/api/v1/like/", json={
    "film_id": film_uuid,
    "like_value": LIKE_RATING_AVG
})
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("like_value") == LIKE_RATING_AVG
    assert response.json().get("user_id") == user_uuid
    assert response.json().get("film_id") == film_uuid

    response = auth_client.get(f"/api/v1/like/{film_uuid}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("like_value") == LIKE_RATING_AVG
    assert response.json().get("user_id") == user_uuid
    assert response.json().get("film_id") == film_uuid


def test_delete_like(auth_client):
    response = auth_client.delete(f"/api/v1/like/{film_uuid}")
    assert response.status_code == status.HTTP_200_OK

    response = auth_client.delete(f"/api/v1/like/{film_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND