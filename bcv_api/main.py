"""BCV API main module."""

from fastapi import FastAPI


from bcv_api import models
from bcv_api.config import settings
from bcv_api.database import engine
from bcv_api.routers import root, users, rates

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    summary=settings.summary,
    description=settings.description,
    version=settings.version,
    contact=settings.contact,
    license_info=settings.license_info,
    openapi_tags=settings.openapi_tags,
)

app.include_router(root.router)
app.include_router(users.router)
app.include_router(rates.router)
