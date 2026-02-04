from uuid import UUID
from beanie import Document, Indexed
from pydantic import Field
from datetime import datetime


class Review(Document):
    film_id: UUID = Indexed(UUID)
    user_id: UUID = Indexed(UUID)
    value: str = Field(
        ...,
        min_length=1,
        max_length=5000
    )
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(default_factory=datetime.now)
