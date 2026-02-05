from fastapi import APIRouter, Depends, Request, status
from uuid import UUID
from models.like import Like
from services import like_service

router = APIRouter(prefix='/like', tags=['likes'])


@router.get("/{film_id}/{user_id}", response_model=Like)
async def get_like(
    film_id: UUID,
    user_id: UUID
) -> Like:
    return await like_service.get_like(film_id=film_id, user_id=user_id)


@router.put("/", response_model=Like, status_code=status.HTTP_201_CREATED)
async def set_like(
    body: Like
) -> Like:
    return await like_service.set_like(body.film_id, body.user_id, body.like_value)


@router.delete("/{film_id}/{user_id}", status_code=status.HTTP_200_OK)
async def delete_like(
    film_id: UUID,
    user_id: UUID
):
    return await like_service.delete_like(film_id=film_id, user_id=user_id)
