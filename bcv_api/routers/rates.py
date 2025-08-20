"""Rates endpoints."""

from datetime import date, timedelta
from typing import Annotated, Optional

from fastapi import Depends, HTTPException, Query

from fastapi import APIRouter
from sqlalchemy.orm import Session

from bcv_api import models, schemas, services, bcv_service, depends

router = APIRouter(
    prefix="/rates",
    tags=["rates"]
)


@router.get("/")
def read_exchange_rate(db: Session = Depends(depends.get_db)) -> schemas.ExchangeRate:
    """# Get the exchange rate for USD from the database.

    This endpoint returns the exchange rate for USD for the current date.

    Returns:
    -------
    schemas.ExchangeRate
    """

    rate = services.get_rate(db)
    if rate is None:
        raise HTTPException(status_code=404, detail="No rates found.")
    return schemas.ExchangeRate(dollar=rate.dollar, date=rate.date)


@router.get("/history")
def read_exchange_rate_history(
    start_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD format)"),
    end_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD format)"),
    db: Session = Depends(depends.get_db)
) -> schemas.ExchangeRateHistory:
    """# Get the exchange rate history within a date range.

    This endpoint returns the exchange rate history for USD within a date range.
    If no dates are provided, returns the last month's data.

    Parameters:
    ----------
    start_date: date, optional
        Start date of the range (format: YYYY-MM-DD)
    end_date: date, optional
        End date of the range (format: YYYY-MM-DD)

    Returns:
    -------
    schemas.ExchangeRateHistory
    """
    # If no dates provided, default to last month
    if start_date is None or end_date is None:
        end_date = date.today()
        start_date = end_date - timedelta(days=30)
    
    # Validate date range
    if start_date > end_date:
        raise HTTPException(status_code=400, detail="Start date must be before or equal to end date")
    
    # Get rates from database
    rates = services.get_rates_by_date_range(db, start_date, end_date)
    
    # Convert to schema format
    exchange_rates = [
        schemas.ExchangeRate(dollar=rate.dollar, date=rate.date) 
        for rate in rates
    ]
    
    return schemas.ExchangeRateHistory(
        start_date=start_date,
        end_date=end_date,
        rates=exchange_rates
    )


@router.get("/{rate_date}")
def read_rate(
    rate_date: date, db: Session = Depends(depends.get_db)
) -> schemas.ExchangeRate:
    """# Get the rate for a specific date from the database.

    Parameters:
    ----------
    rate_date: date
        Date to get the rate for (format: YYYY-MM-DD)

    Returns:
    -------
    schemas.ExchangeRate
    """
    rate = services.get_rate_from_date(db, rate_date)
    if rate is None:
        raise HTTPException(status_code=404, detail="Rate not found")
    return schemas.ExchangeRate(dollar=rate.dollar, date=rate.date)


@router.post("/")
def create_rate(
    token: Annotated[str, Depends(depends.oauth2_scheme)],
    db: Session = Depends(depends.get_db),
) -> schemas.Rate:
    """Create a new rate in the database using the BCV API.

    Parameters:
    ----------
    token: str
        Access token.

    Returns:
    -------
    schemas.Rate
    """
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    dollar_rate = bcv_service.get_exchange_rate()
    rate = services.create_rate(
        db, rate=models.Rate(dollar=dollar_rate, date=date.today())
    )
    return schemas.Rate(dollar=rate.dollar, date=rate.date, id=rate.id)
