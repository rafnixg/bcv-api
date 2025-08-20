"""Services for the BCV API."""

from datetime import date, timedelta
from typing import List

from sqlalchemy.orm import Session

from bcv_api import models, schemas, security
from bcv_api.config import settings

# RATE SERVICES


def get_rate(db: Session) -> models.Rate:
    """Get the last rate from the database.

    Parameters:
    ----------
    db: Session
        Database session.

    Returns:
    -------
    models.Rate
    """
    return db.query(models.Rate).order_by(models.Rate.date.desc()).first()


def get_rate_from_date(db: Session, rate_date: date) -> models.Rate:
    """Get the rate from the database for a specific date.

    Parameters:
    ----------
    db: Session
        Database session.
    rate_date: date
        Rate date.

    Returns:
    -------
    models.Rate
    """
    return (
        db.query(models.Rate)
        .filter(models.Rate.date == rate_date)
        .order_by(models.Rate.id.desc())
        .first()
    )


def get_rates(db: Session, skip: int = 0, limit: int = 100) -> List[models.Rate]:
    """Get all rates from the database.

    Parameters:
    ----------
    db: Session
        Database session.
    skip: int
        Number of records to skip.
    limit: int
        Number of records to return.

    Returns:
    -------
    List[models.Rate]
    """
    return db.query(models.Rate).offset(skip).limit(limit).all()


def get_rates_by_date_range(db: Session, start_date: date, end_date: date) -> List[models.Rate]:
    """Get rates from the database within a date range.

    Parameters:
    ----------
    db: Session
        Database session.
    start_date: date
        Start date of the range.
    end_date: date
        End date of the range.

    Returns:
    -------
    List[models.Rate]
    """
    return (
        db.query(models.Rate)
        .filter(models.Rate.date >= start_date)
        .filter(models.Rate.date <= end_date)
        .order_by(models.Rate.date.desc())
        .all()
    )


def create_rate(db: Session, rate: schemas.Rate) -> models.Rate:
    """Create a new rate in the database.

    Parameters:
    ----------
    db: Session
        Database session.
    rate: schemas.Rate
        Rate to create.

    Returns:
    -------
    models.Rate
    """
    db_rate = get_rate_from_date(db, rate.date)
    if db_rate:
        return update_rate(db, rate)
    db_rate = models.Rate(dollar=rate.dollar, date=rate.date)
    db.add(db_rate)
    db.commit()
    db.refresh(db_rate)
    return db_rate


def update_rate(db: Session, rate: schemas.Rate) -> models.Rate:
    """Update a rate in the database.

    Parameters:
    ----------
    db: Session
        Database session.
    rate: schemas.Rate
        Rate to update.

    Returns:
    -------
    models.Rate
    """
    db_rate = get_rate_from_date(db, rate.date)
    if db_rate:
        db_rate.dollar = rate.dollar
        db.commit()
        db.refresh(db_rate)
    return db_rate


# USER SERVICES


def get_user_by_email(db: Session, email: str) -> models.User:
    """Get a user by email.

    Parameters:
    ----------
    db: Session
        Database session.
    email: str
        User email.

    Returns:
    -------
    models.User
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_user(db: Session, email: str) -> schemas.User | None:
    """Get a user from the database.

    Parameters:
    ----------
    db: Session
        Database session.
    email: str
        User email.

    Returns:
    -------
    schemas.User | None
    """
    user = get_user_by_email(db, email)
    if user:
        return schemas.User(**user)


def authenticate_user(db: Session, username: str, password: str) -> models.User | None:
    """Authenticate a user.

    Parameters:
    ----------
    db: Session
        Database session.
    username: str
        User email.
    password: str
        User password.

    Returns:
    -------
    models.User | None
    """

    user = get_user_by_email(db, username)
    if not user:
        return False
    if not security.verify_password(password, user.hashed_password):
        return False
    return user


def register_user(db: Session, user: schemas.UserCreate) -> models.User:
    """Register a new user.

    Parameters:
    ----------
    db: Session
        Database session.
    user: schemas.UserCreate
        User to create.

    Returns:
    -------
    models.User
    """
    access_token_expires = timedelta(days=settings.access_token_expire_minutes)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    db_user = models.User(
        email=user.email,
        hashed_password=security.get_password_hash(user.password),
        api_key=access_token,
        max_requests=settings.max_requests,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
