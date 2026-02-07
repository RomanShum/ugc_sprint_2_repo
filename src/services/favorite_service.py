from models.entity import Favorite
from fastapi import HTTPException, status


async def get_favorite_from_db(user_id, film_id):
    return await Favorite.find_one(Favorite.user_id == user_id, Favorite.film_id == film_id)

async def get_favorite( user_id, film_id):
    favorite = await get_favorite_from_db(user_id, film_id)
    if not favorite:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Не найдено'
        )
    return favorite

async def set_favorite( user_id, film_id):
    favorite = await get_favorite_from_db(user_id, film_id)
    if not favorite:
        favorite = Favorite(user_id=user_id, film_id=film_id)
        return await favorite.insert()

async def delete_favorite( user_id, film_id):
    favorite = await get_favorite_from_db(user_id, film_id)
    if not favorite:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Не найдено'
        )
    await favorite.delete()
    return True