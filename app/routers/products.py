from fastapi import APIRouter

from ..db import db_select_products

router = APIRouter()

@router.get("/products/", tags=["products"])
async def read_products():
    rows = db_select_products()

    return list(rows)
