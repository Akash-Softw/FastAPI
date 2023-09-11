from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


conn = MongoClient("mongodb+srv://akashmukherjee2908:7cc675bc89c1d9998046ff2615371132@akashcluster.io8ogmc.mongodb.net/notes")
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
   docs = conn.notes.notes.find({})
   print(docs)
   return templates.TemplateResponse("index.html", {"request": request})
