import uuid
from pydantic import BaseModel
from typing import Optional

class BookSchema(BaseModel):
    title: str
    id: str
    description: Optional[str]

class BookSaveSchema(BookSchema):
    slug: str
