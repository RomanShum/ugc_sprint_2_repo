from uuid import UUID
from beanie import Document, Indexed
from pydantic import Field


class Like(Document):
    film_id: UUID = Indexed(UUID)
    user_id: UUID = Indexed(UUID)
    value: int = Field(..., ge=1, le=10)
