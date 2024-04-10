"""Depends module for FastAPI application."""

from typing import Annotated
from jose import JWTError, jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from bcv_api import schemas, services
from bcv_api.config import settings
from bcv_api.database import SessionLocal


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")


def get_db():
    """Get the database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
) -> schemas.User:
    """Get the current user.

    Parameters:
    ----------
    token: str
        Token.
    db: Session
        Database session.

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
    except JWTError:
        raise credentials_exception
    user = services.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[schemas.User, Depends(get_current_user)],
):
    """Get the current active user.

    Parameters:
    ----------
    current_user: schemas.User
        Current user.

    Returns:
    -------
    schemas.User
    """
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
