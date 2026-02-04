from models.review import Review
from fastapi import HTTPException, status
from datetime import datetime

async def get_review_from_db(user_id, film_id):
    return await Review.find_one(Review.user_id == user_id, Review.film_id == film_id)

async def get_review( user_id, film_id):
    review = await get_review_from_db(user_id, film_id)
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Не найдено'
        )
    return review

async def set_review( user_id, film_id, value):
    review = await get_review_from_db(user_id, film_id)
    if review:
        review.value = value
        review.updated = datetime.now()
        return await review.save()
    else:
        review = Review(user_id=user_id, film_id=film_id, value=value)
        return await review.insert()

async def delete_review( user_id, film_id):
    review = await get_review_from_db(user_id, film_id)
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Не найдено'
        )
    await review.delete()
    return True