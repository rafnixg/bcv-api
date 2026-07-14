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
def read_exchange_rate(
    currency: str = Query("USD", description="Currency code (USD, EUR, CNY, TRY, RUB)"),
    db: Session = Depends(depends.get_db)
) -> schemas.ExchangeRate:
    """# Get the exchange rate for a specific currency from the database.

    This endpoint returns the exchange rate for the specified currency for the current date.

    Parameters:
    ----------
    currency: str
        Currency code (default: USD)

    Returns:
    -------
    schemas.ExchangeRate
    """

    rate = services.get_rate(db, currency)
    if rate is None:
        raise HTTPException(status_code=404, detail="No rates found.")
    return schemas.ExchangeRate(rate=rate.rate, currency=rate.currency, date=rate.date)


@router.get("/history")
def read_exchange_rate_history(
    currency: str = Query("USD", description="Currency code (USD, EUR, CNY, TRY, RUB)"),
    start_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD format)"),
    end_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD format)"),
    db: Session = Depends(depends.get_db)
) -> schemas.ExchangeRateHistory:
    """# Get the exchange rate history within a date range for a specific currency.

    This endpoint returns the exchange rate history for the specified currency within a date range.
    If no dates are provided, returns the last month's data.

    Parameters:
    ----------
    currency: str
        Currency code (default: USD)
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
    rates = services.get_rates_by_date_range(db, start_date, end_date, currency)
    
    # Convert to schema format
    exchange_rates = [
        schemas.ExchangeRate(rate=rate.rate, currency=rate.currency, date=rate.date) 
        for rate in rates
    ]
    
    return schemas.ExchangeRateHistory(
        start_date=start_date,
        end_date=end_date,
        rates=exchange_rates
    )


@router.get("/{rate_date}")
def read_rate(
    rate_date: date,
    currency: str = Query("USD", description="Currency code (USD, EUR, CNY, TRY, RUB)"),
    db: Session = Depends(depends.get_db)
) -> schemas.ExchangeRate:
    """# Get the rate for a specific date and currency from the database.

    Parameters:
    ----------
    rate_date: date
        Date to get the rate for (format: YYYY-MM-DD)
    currency: str
        Currency code (default: USD)

    Returns:
    -------
    schemas.ExchangeRate
    """
    rate = services.get_rate_from_date(db, rate_date, currency)
    if rate is None:
        raise HTTPException(status_code=404, detail="Rate not found")
    return schemas.ExchangeRate(rate=rate.rate, currency=rate.currency, date=rate.date)


@router.post("/")
def create_rate(
    currency: str = Query("USD", description="Currency code (USD, EUR, CNY, TRY, RUB)"),
    token: Annotated[str, Depends(depends.oauth2_scheme)] = None,
    db: Session = Depends(depends.get_db),
) -> schemas.Rate:
    """Create a new rate in the database using the BCV API.

    Parameters:
    ----------
    currency: str
        Currency code (default: USD)
    token: str
        Access token.

    Returns:
    -------
    schemas.Rate
    """
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    # Map currencies to BCV div IDs and get rates
    currency_mapping = {
        "USD": "dolar",
        "EUR": "euro", 
        "CNY": "yuan",
        "TRY": "lira",
        "RUB": "rublo"
    }
    
    if currency not in currency_mapping:
        raise HTTPException(status_code=400, detail="Unsupported currency")
    
    try:
        rate_value = bcv_service.get_exchange_rate(currency_mapping[currency])
        rate = services.create_rate(db, rate_value, currency, date.today())
        return schemas.Rate(
            rate=rate.rate, 
            currency=rate.currency, 
            date=rate.date, 
            id=rate.id,
            create_date=rate.create_date,
            update_date=rate.update_date
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
