"""Models for the BCV API."""

from sqlalchemy import Boolean, Column, Integer, String, Date, Float

from bcv_api.database import Base


class User(Base):
    """User model."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    api_key = Column(String)



class Rate(Base):
    """Rate model."""

    __tablename__ = "rates"

    id = Column(Integer, primary_key=True, index=True)
    dollar = Column(Float)
    date = Column(Date, index=True, default=Date())
