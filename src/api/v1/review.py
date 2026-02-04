from fastapi import APIRouter, Depends, Request, status
from uuid import UUID
from models.review import Review
import services.review_service as review_service

router = APIRouter(prefix='/review', tags=['reviews'])


@router.get("/{film_id}/{user_id}", response_model=Review)
async def get_review(
        film_id: UUID,
        user_id: UUID
) -> Review:
    return await review_service.get_review(film_id = film_id, user_id=user_id)

@router.put("/", response_model=Review, status_code=status.HTTP_201_CREATED)
async def set_review(
        body: Review
) -> Review:
    return await review_service.set_review(body.film_id, body.user_id, body.value)


@router.delete("/{film_id}/{user_id}", status_code=status.HTTP_200_OK)
async def delete_review(
        film_id: UUID,
        user_id: UUID
):
    return await review_service.delete_review(film_id = film_id, user_id=user_id)
