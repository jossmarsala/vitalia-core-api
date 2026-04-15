import os
import json
import tempfile

import firebase_admin
from firebase_admin import credentials, firestore, auth

if not firebase_admin._apps:
    # En Render: lee el JSON de credenciales desde una variable de entorno
    # En local: lee desde el archivo firebase_credentials.json
    credentials_json_str = os.getenv("FIREBASE_CREDENTIALS_JSON")

    if credentials_json_str:
        # Modo Render: parsea el JSON del env var y crea un archivo temporal
        credentials_dict = json.loads(credentials_json_str)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
            json.dump(credentials_dict, tmp)
            tmp_path = tmp.name
        cred = credentials.Certificate(tmp_path)
    else:
        # Modo local: usa el archivo físico
        service_account_path = os.getenv(
            "GOOGLE_APPLICATION_CREDENTIALS",
            "./src/database/firebase_credentials.json"
        )
        cred = credentials.Certificate(service_account_path)

    firebase_admin.initialize_app(cred)

db = firestore.client()
auth_client = auth