import codecs
import csv
from fastapi import APIRouter, BackgroundTasks, UploadFile, File, status
from pydantic import BaseModel

from ..logger import logger_debug
from ..db import db_select_brands, db_select_categories, db_insert_many_product, db_insert_many_brand

router = APIRouter()

class Header(BaseModel):
    name: str

class ProductModel(BaseModel):
    barcode: int
    title: str
    url: str
    components: str
    description: str
    category_id: int
    brand_id: int

    def __str__(self) -> str:
        return f'{self.barcode} {self.title} {self.url} {self.components} {self.description} {self.description} {self.category_id} {self.brand_id}'

class BrandModel(BaseModel):
    title : str
    description: str
    url: str
    logo: str

    def __str__(self) -> str:
        return f'{self.title} {self.description} {self.url} {self.logo}'

class CategoryModel(BaseModel):
    id: int
    title: str
    title_en: str
    description:str

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

# Функция для поиска записи по значению поля
def find_record(records: list, key: str, value: str):
    for record in records:
        if record[key].lower() == value.lower():
            return record
    return None

# https://stackoverflow.com/questions/70617121/how-to-upload-a-csv-file-in-fastapi-and-convert-it-into-json
@router.post("/apiai/upload/products/")
def upload_products(file: UploadFile = File(...)):
    if not file:
        return {"message": "No file sent"}
    else:
        csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))

        headers = ["barcode","title","url","components","description","category","brand"]
        for h in headers:
            if not h in csvReader.fieldnames:
                return {"status": status.HTTP_400_BAD_REQUEST, "error": f"bad product csv: there is not [{h}] column"}

        categories = db_select_categories()
        brands = db_select_brands()

        products = []
        products_tuple = []

        for item in csvReader:
            category = find_record(categories, "title", item['category'])
            if not category:
                continue

            brand = find_record(brands, "title", item["brand"])
            if not brand:
                continue

            product = ProductModel(
                barcode = int(item['barcode']) if item.get('barcode') and is_integer(item.get('barcode')) else 0,
                title = item['title'] if item.get('title') else '',
                url = item['url'] if item.get('url') else '',
                components = item['components'] if item.get('components') else '',
                description = item['description'] if item.get('description') else '',
                category_id = category["id"], 
                brand_id = brand["id"]
            )

            products.append(product)

        for item in products:
            # print(f"{item.barcode} {item.title} {item.category_id} {item.brand_id}")
            pt = (item.barcode, item.title, item.url, item.components, item.description, item.category_id, item.brand_id, )
            products_tuple.append(pt)

        file.file.close()

        db_insert_many_product(products_tuple)

        return {"status": status.HTTP_200_OK} 
    
@router.post("/apiai/upload/brands/")
def upload_brands(file: UploadFile = File(...)):
    if not file:
        return {"message": "No file sent"}
    else:
        csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))

        headers = ["title","description","url","logo"]
        for h in headers:
            if not h in csvReader.fieldnames:
                return {"status": status.HTTP_400_BAD_REQUEST, "error": f"bad product csv: there is not [{h}] column"}

        brands = []
        brands_tuple = []

        for item in csvReader:
            brand = BrandModel(
                title = item['title'] if item.get('title') else '',
                description = item['description'] if item.get('description') else '',
                url = item['url'] if item.get('url') else '',
                logo = item['logo'] if item.get('logo') else ''
            )

            brands.append(brand)

        for item in brands:
            # print(f"{item.title} {item.description} {item.url} {item.logo}")
            bt = (item.title, item.description, item.url, item.logo, )
            brands_tuple.append(bt)

        file.file.close()

        db_insert_many_brand(brands_tuple)

        return {"status": status.HTTP_200_OK} 