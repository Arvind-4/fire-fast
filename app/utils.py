import uuid
from firebase_admin import firestore

from app.shortcuts import get_slug

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
