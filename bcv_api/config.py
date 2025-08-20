"""Configurations for the FastAPI app."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the FastAPI app."""
    
    model_config = {"env_file": ".env", "extra": "ignore"}

    app_name: str = "BCV API"
    summary: str = "API to get the exchange rate for USD from the BCV"
    description: str = """This API allows you to get the exchange rate for USD from the BCV (Banco Central de Venezuela). 🚀

    - / [GET]: Get the exchange rate for USD from the database.
    - / [POST] Create a new rate in the database using the BCV API.
    - /{rate_date} [GET]: Get the rate for a specific date from the database.
    - /token [POST]: Login endpoint to get a JWT token.
    - /users/me [GET]: Get the current user information.
    """
    version: str = "0.2.0"
    admin_email: str = "rafnixg@gmail.com"
    contact: dict = {
        "name": "Rafnix Guzmán",
        "email": "rafnixg@gmail.com",
        "url": "https://links.rafnixg.dev",
    }
    license_info: dict = {
        "name": "GPLv3",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
    }
    openapi_tags: list[dict] = [
        {
            "name": "users",
            "description": "Operations with users. The **login** logic is here.",
        },
        {
            "name": "rates",
            "description": "Operations with rates. Get the **exchange rate** for USD from the BCV.",
        },
    ]
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    sql_alchemy_database_url: str = "sqlite:///./sql_app.db"
    max_requests: int = 10


settings = Settings()


# SECRET_KEY = "62e94b69a99f112d805db42aee22b3c62533d6fdf7bb1d3c1e2a352dbec476a0"
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# MAX_REQUESTS = 10
