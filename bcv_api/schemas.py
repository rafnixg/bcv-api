"""Schemas for the API."""

from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel


class ExchangeRate(BaseModel):
    """Exchange rate for a currency."""

    rate: float
    currency: str
    date: date


class ExchangeRateHistory(BaseModel):
    """Exchange rate history response."""

    start_date: date
    end_date: date
    rates: List[ExchangeRate]


class User(BaseModel):
    """User model."""

    email: str
    hashed_password: str
    is_active: bool
    api_key: str
    id: int
    create_date: Optional[datetime] = None
    update_date: Optional[datetime] = None

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    """User creation model."""

    email: str
    password: str


class Rate(BaseModel):
    """Rate model."""

    rate: float
    currency: str
    date: date
    id: int
    create_date: Optional[datetime] = None
    update_date: Optional[datetime] = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    """Token model."""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token data model."""

    email: str | None = None
