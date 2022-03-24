from fastapi import FastAPI
from firebase_admin import firestore

from app.db import initialize_firebase
from app.books.routers import router as book_router
from app.utils import file_upload
from app.encrypt import (
    encrypt_dir,
    decrypt_dir
)

app = FastAPI()

app.include_router(book_router)
INITIALIZE_FIREBASE = None

@app.on_event("startup")
async def startup_event():
    encrypt_dir()
    decrypt_dir()
    global INITIALIZE_FIREBASE
    INITIALIZE_FIREBASE = initialize_firebase()
    print("Firebase initialized.")

@app.get("/")
async def home():
    # file_upload()
    return {"message": "Hello World"}