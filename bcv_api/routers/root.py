"""Root router for the BCV API."""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def index():
    """Welcome message for the BCV API home page."""
    return {"message": "Welcome to the BCV API! Visit /docs for more information."}
