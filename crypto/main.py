from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory=" templates ")


@app.get("/")
async def dashboard(request: Request):
    """""
    displayes dashoard
    """""
    return templates.TemplateResponse('main.html',{
        "request" : request
    })

@app.post("/stock")
def create_stock():
    """""
    creates a stock and saves it to database
    """""

    return {
        "code":"success",
        "message":"created"
    }

