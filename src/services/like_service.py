from models.entity import Like
from fastapi import HTTPException, status

async def get_like_from_db(user_id, film_id):
    return await Like.find_one(Like.user_id == user_id, Like.film_id == film_id)

async def get_like( user_id, film_id):
    like = await get_like_from_db(user_id, film_id)
    if not like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Не найдено'
        )
    return like

async def set_like( user_id, film_id, like_value):
    # Проверяем, есть ли уже лайк
    like = await get_like_from_db(user_id, film_id)
    if like:
        # Обновляем значение
        like.like_value = like_value
        return await like.save()
    else:
        # Создаём новый
        like = Like(user_id=user_id, film_id=film_id, like_value=like_value)
        return await like.insert()

async def delete_like( user_id, film_id):
    like = await get_like_from_db(user_id, film_id)
    if not like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Не найдено'
        )
    await like.delete()
    return True