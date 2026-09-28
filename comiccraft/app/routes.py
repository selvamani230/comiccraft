from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from app.exporters import save_pdf
from app.image_generator import generate_image

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
COMICS = {}

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {})

@router.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, story: str = Form(...), panels: int = Form(4)):
    images = []
    for i in range(1, panels + 1):
        images.append(generate_image(f"{story} - scene {i}", i))
    COMICS["1"] = {"story": story, "images": images}
    return templates.TemplateResponse(request, "comic_preview.html", {"story": story, "images": images})

@router.get("/export/{comic_id}", response_class=HTMLResponse)
async def export_pdf(request: Request, comic_id: str):
    comic = COMICS.get(comic_id)
    if comic is None:
        return templates.TemplateResponse(request, "export_success.html", {
            "images": [],
            "pdf_path": "/",
        })

    project_dir = os.path.dirname(os.path.dirname(__file__))
    layout = []
    for i, image_url in enumerate(comic["images"], start=1):
        layout.append({
            "title": f"Panel {i}",
            "scene_description": comic["story"],
            "text": "",
            "image_path": os.path.join(project_dir, "static", "panels", f"panel_{i}.png"),
        })

    pdf_path = save_pdf(layout).replace("\\", "/")
    return templates.TemplateResponse(request, "export_success.html", {
        "images": comic["images"],
        "pdf_path": f"/{pdf_path}",
    })