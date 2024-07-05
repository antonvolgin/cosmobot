import requests

from enum import Enum
from fastapi import APIRouter, status
from pydantic import BaseModel

from ..db import db_select_products, db_select_product
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

@router.get("/products/", tags=["products"])
async def read_products():
    rows = db_select_products()

    return {"status": status.HTTP_200_OK, "data": list(rows)}

@router.get("/product/{barcode}")
async def read_product(barcode: int):
    row = db_select_product(barcode)

    if row:
        return {"status": status.HTTP_200_OK, "data": row}
    
    return {"status": status.HTTP_404_NOT_FOUND, "data": None}

@router.get("/suggestions/")
async def get_suggestions(param: ParamSuggestion):
    logger_debug(f"param: {param}")

    row = None

    url = "https://cosmocode.site/api/free/{}".format(param.category)
    params = dict(ingredients=param.ingredients)
    headers = {
        "Content-Type":"application/json",
        "Authorization":"Token jXxtbRXhk7z6G01AGimEKP1j7UGLC_bmecIZa3wgMv9s3QrBBSlkVtqLeafuaLYmuOO5PjgdX6kSkqNTX2jg5A"
    }

    response = requests.post(url=url, headers=headers, json=params)
    
    logger_debug(f"response.headers: {response.headers}\nresponse.status: {response.status_code}")

    if response.status_code == status.HTTP_200_OK:
        logger_debug(f"response: {response.json()}")
        return {"status": status.HTTP_200_OK, "data": response.json()}
  
    return {"status": status.HTTP_404_NOT_FOUND, "data": None}
