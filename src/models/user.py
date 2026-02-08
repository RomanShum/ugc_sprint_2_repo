from uuid import UUID
from beanie import Document, Indexed
from pydantic import Field
from core.settings import Settings

settings = Settings()

class User(Document):
    id: UUID = Indexed(UUID)