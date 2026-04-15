import os
import json
import tempfile

import firebase_admin
from firebase_admin import credentials, firestore, auth

if not firebase_admin._apps:
    # Puede estar en cualquiera de estas dos variables según dónde lo configuraste
    raw_cred = os.getenv("FIREBASE_CREDENTIALS_JSON") or os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    if raw_cred and raw_cred.strip().startswith("{"):
        # El usuario ha pegado el JSON como texto plano en las variables de entorno
        credentials_dict = json.loads(raw_cred)
        cred = credentials.Certificate(credentials_dict)
    else:
        # Busca el archivo local físico
        file_path = raw_cred if raw_cred else "./src/database/firebase_credentials.json"
        cred = credentials.Certificate(file_path)

    firebase_admin.initialize_app(cred)

db = firestore.client()
auth_client = auth