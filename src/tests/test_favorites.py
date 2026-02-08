from fastapi import status
from core.settings import Settings
from constants import film_uuid, user_uuid

settings = Settings()

def test_create_favorite(auth_client):
    response = auth_client.put(f"/api/v1/favorite/", json={
    "film_id": film_uuid
})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json().get("user_id") == user_uuid
    assert response.json().get("film_id") == film_uuid

    response = auth_client.put(f"/api/v1/favorite/", json={
        "film_id": film_uuid
    })
    assert response.status_code == status.HTTP_409_CONFLICT

def test_get_favorite(auth_client):
    response = auth_client.get(f"/api/v1/favorite/{film_uuid}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("user_id") == user_uuid
    assert response.json().get("film_id") == film_uuid


def test_delete_favorite(auth_client):
    response = auth_client.delete(f"/api/v1/favorite/{film_uuid}")
    assert response.status_code == status.HTTP_200_OK

    response = auth_client.delete(f"/api/v1/favorite/{film_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND