"""Security module for BCV API."""

from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt

from fastapi import HTTPException, status

from bcv_api import schemas
from bcv_api.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify the password.

    Parameters:
    ----------
    plain_password: str
        Plain password.
    hashed_password: str
        Hashed password.

    Returns:
    -------
    bool
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Get the password hash.

    Parameters:
    ----------
    password: str
        Password to hash.

    Returns:
    -------
    str
    """
    return pwd_context.hash(password)


def get_api_key(email: str) -> str:
    """Get the API key.

    Parameters:
    ----------
    email: str
        User email.

    Returns:
    -------
    str
    """
    return pwd_context.hash(email)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Create an access token using JWT.

    Parameters:
    ----------
    data: dict
        Data to encode.
    expires_delta: timedelta | None
        Expiration time.

    Returns:
    -------
    str
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def verify_access_token(token: str) -> schemas.User:
    """Verify the access token.

    Parameters:
    ----------
    token: str
        Access token.

    Returns:
    -------
    schemas.User
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except jwt.JWTError:
        raise credentials_exception
    return token_data
