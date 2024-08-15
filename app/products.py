from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .db import db_select_products

BASE_DIR = Path(__file__).resolve().parent

router = APIRouter()

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
router.mount("/static", StaticFiles(directory=str(Path(BASE_DIR, "static"))), name="static")

ITEMS_PER_PAGE = 30

@router.get("/apiai/back/products", response_class=HTMLResponse)
async def products(request: Request, page: int = 1, filter: str = ""):
    items, total_items = db_select_products(page, ITEMS_PER_PAGE, filter)
    total_pages = (total_items + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

    # print(f"page:{page} total items:{total_items} total_pages:{total_pages}")
    return templates.TemplateResponse("products.html", {
        "request": request, 
        "items": items, 
        "page": page, 
        "total_pages": total_pages,
        "filter": filter,
    })