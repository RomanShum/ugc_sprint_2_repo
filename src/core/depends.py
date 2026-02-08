from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from core.settings import settings
from fastapi.security import HTTPBearer
from fastapi import Depends
from jose import jwt, JWTError
from uuid import UUID
from typing import Annotated
async def get_current_user(
        token: str = Annotated[str, Depends(HTTPBearer())]
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Ошибка аутентификации"
    )
    try:
        payload = jwt.decode(token.credentials, settings.secret_key,
                             algorithms=[settings.algorithm])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        return UUID(user_id)
    except JWTError:
        raise credentials_exception

def decode_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, settings.secret_key,
                             algorithms=[settings.algorithm])
        return payload
    except JWTError:
        return None