from jose import jwt, JWTError
from fastapi import Depends,HTTPException,status
from passlib.context import CryptContext
from typing import Any,Annotated
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from models.token import TokenData
from database.mongo_driver import get_database,validate_bson_id


_jwt_key: str = 'randomkey'


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, _jwt_key, algorithm='HS512')
    return encoded_jwt

def decode_jwt_token(token: str) -> dict[str, Any]:
    return jwt.decode(token, _jwt_key, algorithms=['HS512'])


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return plain_password== hashed_password


def get_password_hash(password):
    return password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_user(id):
    bson_id = validate_bson_id(id)
    return await  get_database().get_collection('user').find_one({'_id':bson_id})


async def auth_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, _jwt_key, algorithms=['HS512'])
        userId: str = payload.get("userId")
        if userId is None:
            raise credentials_exception
        token_data = TokenData(userID=userId)
    except JWTError:
        raise credentials_exception
    user = await get_user(token_data.userID)

    if user is None:
        raise credentials_exception
    return token_data.userID


