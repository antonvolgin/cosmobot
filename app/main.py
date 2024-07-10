from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .routers import products, upload
from .db import db_select_products

app = FastAPI(docs_url="/apiai/docs", redoc_url=None)

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
app.mount("/static", StaticFiles(directory=str(Path(BASE_DIR, "static"))), name="static")

app.include_router(products.router)
app.include_router(upload.router)

@app.get("/apiai")
async def root():
    return {"message": "Hello Cosmocode: APIAI!"}

ITEMS_PER_PAGE = 30

@app.get("/apiai/back", response_class=HTMLResponse)
async def products(request: Request, page: int = 1, filter: str = ""):
    items, total_items = db_select_products(page, ITEMS_PER_PAGE, filter)
    total_pages = (total_items + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

    # print(f"page:{page} total items:{total_items} total_pages:{total_pages}")
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "items": items, 
        "page": page, 
        "total_pages": total_pages,
        "filter": filter,
    })