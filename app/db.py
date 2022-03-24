import os
import pathlib
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import (
    firestore,
    credentials
)

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

load_dotenv()

PRODUCTION = str(os.environ.get("PRODUCTION", "false"))
FIREBASE_STROAGE_BUCKET_URL = str(os.environ.get("FIREBASE_STROAGE_BUCKET_URL"))

if PRODUCTION == "true":
    FIREBASE_CREDENTIAL_FILE = BASE_DIR / 'decrypt' / 'secret.json'
else:
    FIREBASE_CREDENTIAL_FILE = BASE_DIR / 'ignored' / 'secret.json'

def initialize_firebase():
    cred = {
        "storageBucket": FIREBASE_STROAGE_BUCKET_URL
    }
    certificate = credentials.Certificate(str(FIREBASE_CREDENTIAL_FILE))
    session = firebase_admin.initialize_app(certificate, cred)
    return session
    