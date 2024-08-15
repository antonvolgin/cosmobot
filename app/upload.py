from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent

router = APIRouter()

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
router.mount("/static", StaticFiles(directory=str(Path(BASE_DIR, "static"))), name="static")

@router.get("/apiai/back/uploads", response_class=HTMLResponse)
async def uploads(request: Request):
    return templates.TemplateResponse("uploads.html", {
        "request": request
})
