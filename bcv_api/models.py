"""Models for the BCV API."""

from sqlalchemy import Boolean, Column, Integer, String, Date, Float, DateTime
from sqlalchemy.sql import func

from bcv_api.database import Base


class User(Base):
    """User model."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
    api_key = Column(String)
    requests = Column(Integer, default=0)
    max_requests = Column(Integer, default=10)
    create_date = Column(DateTime, default=func.now())
    update_date = Column(DateTime, default=func.now(), onupdate=func.now())


class Rate(Base):
    """Rate model."""

    __tablename__ = "rates"

    id = Column(Integer, primary_key=True, index=True)
    rate = Column(Float)
    currency = Column(String, default="USD")
    date = Column(Date, index=True, default=Date())
    create_date = Column(DateTime, default=func.now())
    update_date = Column(DateTime, default=func.now(), onupdate=func.now())
