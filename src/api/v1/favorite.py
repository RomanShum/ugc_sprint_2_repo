from fastapi import APIRouter, Depends, Request, status
from uuid import UUID
from models.entity import Favorite
from services import favorite_service

router = APIRouter(prefix='/favorite', tags=['favorites'])


@router.get("/{film_id}/{user_id}", response_model=Favorite)
async def get_favorite(
    film_id: UUID,
    user_id: UUID
) -> Favorite:
    return await favorite_service.get_favorite(film_id=film_id, user_id=user_id)


@router.put("/", response_model=Favorite, status_code=status.HTTP_201_CREATED)
async def set_favorite(
    body: Favorite
) -> Favorite:
    return await favorite_service.set_favorite(body.film_id, body.user_id)


@router.delete("/{film_id}/{user_id}", status_code=status.HTTP_200_OK)
async def delete_favorite(
    film_id: UUID,
    user_id: UUID
):
    return await favorite_service.delete_favorite(film_id=film_id, user_id=user_id)
