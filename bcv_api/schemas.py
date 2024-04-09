"""Schemas for the API."""

from datetime import date
from pydantic import BaseModel


class ExchangeRate(BaseModel):
    """Exchange rate for USD."""

    dollar: float
    date: date


class User(BaseModel):
    """User model."""

    email: str
    hashed_password: str
    is_active: bool
    api_key: str
    id: int


class Rate(BaseModel):
    """Rate model."""

    dollar: float
    date: date
    id: int

    class Config:
        orm_mode = True
