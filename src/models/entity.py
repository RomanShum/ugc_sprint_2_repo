from uuid import UUID
from beanie import Document, Indexed
from pydantic import Field
from datetime import datetime
from core.settings import Settings

settings = Settings()

class Favorite(Document):
    film_id: UUID = Indexed(UUID)
    user_id: UUID = Indexed(UUID)

class Like(Document):
    film_id: UUID = Indexed(UUID)
    user_id: UUID = Indexed(UUID)
    like_value: int = Field(..., ge=1, le=10)

class Review(Document):
    film_id: UUID = Indexed(UUID)
    user_id: UUID = Indexed(UUID)
    review_value: str = Field(
        ...,
        min_length=settings.min_review_length,
        max_length=settings.max_review_length
    )
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(default_factory=datetime.now)