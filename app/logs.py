from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .db import db_select_logs

BASE_DIR = Path(__file__).resolve().parent

router = APIRouter()

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
router.mount("/static", StaticFiles(directory=str(Path(BASE_DIR, "static"))), name="static")

ITEMS_PER_PAGE = 30

@router.get("/apiai/back/logs", response_class=HTMLResponse)
async def get_logs(request: Request, page: int = 1, filter: str = "", products: str = "products_all", created_at_order: str = "DESC"):
    items, total_items = db_select_logs(page, ITEMS_PER_PAGE, filter, products, created_at_order)
    total_pages = (total_items + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

    products_options = [
        {"value": "products_all", "label": "All"},
        {"value": "products_not_found", "label": "Not Found"},
        {"value": "products_found", "label": "Found"},
    ]

    return templates.TemplateResponse("logs.html", {
        "request": request,
        "items": items, 
        "page": page, 
        "total_pages": total_pages,
        "filter": filter,
        "products_options": products_options,
        "products": products,
})
