import os
import uuid
import pathlib
from firebase_admin import (
    firestore,
    storage,
)

from app.shortcuts import get_slug

IMAGE_PATH = pathlib.Path(__file__).resolve().parent.parent
IMAGE_FOLDER_PATH = IMAGE_PATH / 'images'

IMAGE_FILE_NAME = IMAGE_FOLDER_PATH / '1.jpg'
IMAGE_UPLOAD_FILE_NAME = str(IMAGE_FILE_NAME.name)

IMAGE_CLOULD_STORAGE_FOLDER = 'Images'
IMAGE_BLOB_NAME = f"{IMAGE_CLOULD_STORAGE_FOLDER}/{IMAGE_UPLOAD_FILE_NAME}"

def get_all():
    db = firestore.client()
    collection = db.collection("books")
    document_list = [document.to_dict() for document in collection.stream()]
    return document_list


def save(data: dict):
    title = str(data.get('title'))
    id_ = str(data.get('id'))
    description = str(data.get('description', ""))
    slug = get_slug(title)

    if not id_:
        id_ = str(uuid.uuid4())

    db = firestore.client()
    collection = db.collection("books")
    document = collection.document(slug)
    result = document.set({
        "id": id_,
        "title": title,
        "description": description,
        "slug": slug,
    })
    print('From utils.save()', result)
    return data

def get_one(slug: str):
    db = firestore.client()
    collection = db.collection("books")
    document = errors = {}
    try:
        document = collection.document(slug).get()
        print('From utils.get_one()', document.to_dict())
    except Exception as e:
        errors['error'] = str(e)
    return document.to_dict(), errors

def update_data(slug: str, data: dict):
    db = firestore.client()
    collection = db.collection("books")
    document = errors = {}
    try:
        document = collection.document(slug).update(data)
    except Exception as e:
        errors['error'] = str(e)
    return document, errors

def delete_data(slug: str):
    errors = {}
    result = None
    db = firestore.client()
    collection = db.collection("books")
    document = collection.document(slug)
    try:
        result = document.delete()
    except Exception as e:
        errors['error'] = str(e)
    return result, errors

def file_upload():
    bucket = storage.bucket()
    imageBlob = bucket.blob(str(IMAGE_BLOB_NAME))
    imageUploadpath = str(IMAGE_FILE_NAME)
    imageBlob.upload_from_filename(str(imageUploadpath))