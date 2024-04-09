"""BCV API main module."""

from datetime import date
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from bcv_api import models, services, schemas, bcv_service
from bcv_api.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_exchange_rate(db: Session = Depends(get_db)) -> schemas.ExchangeRate:
    """Get the exchange rate for USD from BCV"""
    rate = services.get_rate(db)
    return schemas.ExchangeRate(dollar=rate.dollar, date=rate.date)


@app.get("/{rate_date}")
def read_rate(rate_date: date, db: Session = Depends(get_db)) -> schemas.ExchangeRate:
    """Get the rate for a specific date."""
    rate = services.get_rate_from_date(db, rate_date)
    if rate is None:
        raise HTTPException(status_code=404, detail="Rate not found")
    return schemas.ExchangeRate(dollar=rate.dollar, date=rate.date)


@app.post("/")
def create_rate(db: Session = Depends(get_db)) -> schemas.Rate:
    """Create a new rate."""
    dollar_rate = bcv_service.get_exchange_rate()
    rate = services.create_rate(db, rate=models.Rate(dollar=dollar_rate, date=date.today()))
    return schemas.Rate(dollar=rate.dollar, date=rate.date, id=rate.id)
