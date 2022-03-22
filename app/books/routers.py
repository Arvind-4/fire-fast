from fastapi import APIRouter
from firebase_admin import firestore
from typing import List

from app.utils import (
    save,
    get_all,
    get_one,
)
from .schemas import (
    BookSchema,
    BookSaveSchema,
)

router = APIRouter()

@router.get('/books/', response_model=List[BookSaveSchema], status_code=200)
async def get_books():
    document_list = get_all()
    return document_list

@router.post('/books/create/', response_model=BookSchema, status_code=200)
async def save_books(book_data: BookSchema):
    data = save(dict(book_data))
    return data

@router.get('/books/{slug}/', response_model=BookSaveSchema, status_code=200)
async def get_book(slug: str):
    data, errors = get_one(slug)
    if len(errors) > 0:
        return errors
    return data

@router.post('/books/{slug}/delete/')
async def delete_book(slug: str):
    db = firestore.client()
    collection = db.collection("books")
    document = collection.document(slug)
    result = document.delete()
    return result