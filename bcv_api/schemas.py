"""Schemas for the API."""

from datetime import date
from typing import List
from pydantic import BaseModel


class ExchangeRate(BaseModel):
    """Exchange rate for USD."""

    dollar: float
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

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    """User creation model."""

    email: str
    password: str


class Rate(BaseModel):
    """Rate model."""

    dollar: float
    date: date
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    """Token model."""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token data model."""

    email: str | None = None
