from fastapi import Request, HTTPException, Depends, status
from firebase_admin import auth
from src.database.database_connection import auth_client

async def get_current_user(request: Request):
    """
    Extrae y verifica el token Firebase del header Authorization: Bearer <token>.
    """
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token no provisto",
        )

    token = auth_header.split(" ")[1]

    try:
        decoded_token = auth_client.verify_id_token(token)
        return decoded_token 
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token inválido: {e}",
        )
