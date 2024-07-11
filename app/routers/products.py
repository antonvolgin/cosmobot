import requests

from enum import Enum
from fastapi import APIRouter, status
from pydantic import BaseModel

from ..db import db_select_products, db_select_product, db_insert_log, db_select_brands, db_select_categories, db_select_logs
from ..logger import logger_debug

router = APIRouter()

class Category(str, Enum):
    shampoo = "shampoo"
    balzam = "balzam"
    stayling = "stayling"
    piling = "piling"

class ParamSuggestion(BaseModel):
    category: Category
    ingredients: str

@router.get("/apiai/products/", tags=["products"])
async def read_products():
    rows, total = db_select_products()

    return {"status": status.HTTP_200_OK, "items": list(rows), "total": total}

@router.get("/apiai/product/{barcode}")
async def read_product(barcode: int):
    row = db_select_product(barcode)

    if row:
        db_insert_log(barcode, row["id"])
        return {"status": status.HTTP_200_OK, "data": row}

    db_insert_log(barcode, None)
    return {"status": status.HTTP_404_NOT_FOUND, "data": None}

@router.post("/apiai/suggestions/")
async def get_suggestions(param: ParamSuggestion):
    logger_debug(f"suggestions: param: {param}")

    url = "https://cosmocode.site/api/free/{}".format(param.category)
    params = dict(ingredients=param.ingredients)
    headers = {
        "Content-Type":"application/json",
        "Authorization":"Token jXxtbRXhk7z6G01AGimEKP1j7UGLC_bmecIZa3wgMv9s3QrBBSlkVtqLeafuaLYmuOO5PjgdX6kSkqNTX2jg5A"
    }

    response = requests.post(url=url, headers=headers, json=params)
    
    # logger_debug(f"response.headers: {response.headers}\nresponse.status: {response.status_code}")

    if response.status_code == status.HTTP_200_OK:
        # logger_debug(f"response: {response.json()}")
        return {"status": status.HTTP_200_OK, "data": response.json()}
  
    return {"status": status.HTTP_404_NOT_FOUND, "data": None}

@router.get("/apiai/brands/", tags=["brands"])
async def read_brands():
    rows = db_select_brands()

    return {"status": status.HTTP_200_OK, "data": list(rows)}

@router.get("/apiai/categories/", tags=["categories"])
async def read_categories():
    rows = db_select_categories()

    return {"status": status.HTTP_200_OK, "data": list(rows)}

@router.get("/apiai/logs/", tags=["logs"])
async def read_logs():
    rows = db_select_logs()

    return {"status": status.HTTP_200_OK, "data": list(rows)}
