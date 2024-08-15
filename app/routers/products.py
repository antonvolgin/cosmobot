import csv
from io import StringIO
import sqlite3
from fastapi.responses import StreamingResponse
import requests

from enum import Enum
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from ..db import db_select_products, db_select_product, db_insert_log, db_select_brands, db_select_categories, db_select_logs, db_create_connection
from ..logger import logger_debug

router = APIRouter()

class Category(str, Enum):
    shampoo = "shampoo"
    balsam = "balsam"
    styling = "styling"

class ParamSuggestion(BaseModel):
    category: Category
    ingredients: str

@router.get("/apiai/products/", tags=["products"])
async def read_products():
    rows, total = db_select_products(per_page=1_000_000_000)

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

def iter_csv(cursor):
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)

    # Записываем заголовки
    headers = [description[0] for description in cursor.description]
    print(f"headers: {headers}")
    writer.writerow(headers)
    yield csv_buffer.getvalue()
    csv_buffer.seek(0)
    csv_buffer.truncate(0)

    # Записываем строки по одной порции
    while True:
        rows = cursor.fetchmany(1000)  # Читаем порциями по 1000 строк
        if not rows:
            break
        for row in rows:
            writer.writerow(row)
        yield csv_buffer.getvalue()
        csv_buffer.seek(0)
        csv_buffer.truncate(0)

    cursor.connection.close()

@router.get("/apiai/logs_csv/", tags=["logs_csv"])
async def read_logs_csv():
    try:
        conn = db_create_connection()
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM log ORDER BY created_at DESC")

        # Возвращаем CSV файл как потоковый ответ
        response = StreamingResponse(iter_csv(cursor), media_type="text/csv")
        response.headers["Content-Disposition"] = f"attachment; filename=logs.csv"
        return response

    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
