"""Scrapper for https://www.bcv.org.ve/ getting the exchange rate for multiple currencies"""

import requests
from bs4 import BeautifulSoup


def get_exchange_rate(currency: str = "dolar") -> float:
    """Get the exchange rate for a specific currency from https://bcv.org.ve
    
    Args:
        currency: Currency to get rate for. Options: dolar, euro, yuan, lira, rublo
        
    Returns:
        Exchange rate as float
    """
    url = "https://bcv.org.ve"
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, "html.parser")
    div_currency = soup.find(id=currency)
    
    if div_currency is None:
        raise ValueError(f"Currency '{currency}' not found on BCV website")
        
    div_amount = div_currency.find_all(class_="col-sm-6 col-xs-6 centrado")[0].get_text()
    format_amount = round(float(div_amount.strip().replace(",", ".")), 4)
    return format_amount


def get_usd_rate() -> float:
    """Get USD exchange rate (for backward compatibility)"""
    return get_exchange_rate("dolar")


def get_euro_rate() -> float:
    """Get EUR exchange rate"""
    return get_exchange_rate("euro")


def get_yuan_rate() -> float:
    """Get CNY exchange rate"""
    return get_exchange_rate("yuan")


def get_lira_rate() -> float:
    """Get TRY exchange rate"""
    return get_exchange_rate("lira")


def get_rublo_rate() -> float:
    """Get RUB exchange rate"""
    return get_exchange_rate("rublo")
