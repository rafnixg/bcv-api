"""Services for the BCV API."""
from datetime import date
from typing import List

from sqlalchemy.orm import Session

from bcv_api import models, schemas


def get_rate(db: Session) -> models.Rate:
    """Get the last rate from the database."""
    return db.query(models.Rate).order_by(models.Rate.date.desc()).first()

def get_rate_from_date(db: Session, date: date) -> models.Rate:
    """Get the rate from the database for a specific date."""
    return db.query(models.Rate).filter(models.Rate.date == date).order_by(models.Rate.id.desc()).first()

def get_rates(db: Session, skip: int = 0, limit: int = 100) -> List[models.Rate]:
    """Get all rates from the database."""
    return db.query(models.Rate).offset(skip).limit(limit).all()

def create_rate(db: Session, rate: schemas.Rate) -> models.Rate:
    """Create a new rate in the database."""
    db_rate = get_rate_from_date(db, rate.date)
    if db_rate:
        return update_rate(db, rate)
    db_rate = models.Rate(
        dollar=rate.dollar,
        date=rate.date
    )
    db.add(db_rate)
    db.commit()
    db.refresh(db_rate)
    return db_rate

def update_rate(db: Session, rate: schemas.Rate) -> models.Rate:
    """Update a rate in the database."""
    db_rate = get_rate_from_date(db, rate.date)
    if db_rate:
        db_rate.dollar = rate.dollar
        db.commit()
        db.refresh(db_rate)
    return db_rate
