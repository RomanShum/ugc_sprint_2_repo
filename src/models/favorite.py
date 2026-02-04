from uuid import UUID
from beanie import Document, Indexed
from pydantic import Field


class Favorite(Document):
    film_id: UUID = Indexed(UUID)
    user_id: UUID = Indexed(UUID)
