"""Users endpoints."""

from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from fastapi import APIRouter
from sqlalchemy.orm import Session

from bcv_api import schemas, services, depends, security
from bcv_api.config import settings

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/token", response_model=schemas.Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(depends.get_db)],
):
    """# Login endpoint to get a JWT token.

    Parameters:
    ----------
    **form_data**: OAuth2PasswordRequestForm
        - username: str
        - password: str

    Returns:
    -------
    schemas.Token
    """
    user = services.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")


@router.get("/me", response_model=schemas.User)
async def read_users_me(
    current_user: Annotated[schemas.User, Depends(depends.get_current_active_user)]
):
    """# Get the current user information."""
    return current_user


@router.post("/", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate, db: Annotated[Session, Depends(depends.get_db)]
):
    """# Create a new user.

    Parameters:
    ----------
    **user**: schemas.UserCreate
        - email: str
        - password: str

    Returns:
    -------
    schemas.User
    """
    db_user = services.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return services.register_user(db, user)
