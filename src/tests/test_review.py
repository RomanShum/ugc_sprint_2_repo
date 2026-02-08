from fastapi import status
from core.settings import Settings
# from tools import film_uuid, user_uuid
from constants import REVIEW_VALUE_TEST, REVIEW_VALUE_TEST1, film_uuid, user_uuid

settings = Settings()

def test_create_review(auth_client):
    response = auth_client.post(f"/api/v1/review/", json={
    "film_id": film_uuid,
    "review_value": REVIEW_VALUE_TEST
})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json().get("review_value") == REVIEW_VALUE_TEST
    assert response.json().get("user_id") == user_uuid
    assert response.json().get("film_id") == film_uuid

    response = auth_client.post(f"/api/v1/review/", json={
        "film_id": film_uuid,
        "review_value": REVIEW_VALUE_TEST
    })
    assert response.status_code == status.HTTP_409_CONFLICT

def test_get_review(auth_client):
    response = auth_client.get(f"/api/v1/review/{film_uuid}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("review_value") == REVIEW_VALUE_TEST
    assert response.json().get("user_id") == user_uuid
    assert response.json().get("film_id") == film_uuid

def test_patch_and_get_review(auth_client):
    response = auth_client.patch(f"/api/v1/review/", json={
    "film_id": film_uuid,
    "review_value": REVIEW_VALUE_TEST1
})
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("review_value") == REVIEW_VALUE_TEST1
    assert response.json().get("user_id") == user_uuid
    assert response.json().get("film_id") == film_uuid

    response = auth_client.get(f"/api/v1/review/{film_uuid}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("review_value") == REVIEW_VALUE_TEST1
    assert response.json().get("user_id") == user_uuid
    assert response.json().get("film_id") == film_uuid


def test_delete_review(auth_client):
    response = auth_client.delete(f"/api/v1/review/{film_uuid}")
    assert response.status_code == status.HTTP_200_OK

    response = auth_client.delete(f"/api/v1/review/{film_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND