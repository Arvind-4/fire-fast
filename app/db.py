import os
import pathlib
from dotenv import load_dotenv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

load_dotenv()

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

FIREBASE_CREDENTIAL_FILE = BASE_DIR / 'secret.json'

def initialize_firebase():
    cred = credentials.Certificate(str(FIREBASE_CREDENTIAL_FILE))
    session = firebase_admin.initialize_app(cred)
    return session
    