import models
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db import SessionLocal, engine
from pydantic import BaseModel

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

class StockRequest(BaseModel):
    symbol:str

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def dashboard(request: Request):
    """""
    displayes dashoard
    """""
    return templates.TemplateResponse('main.html',{
        "request" : request
    })

@app.post("/stock")
def create_stock(stock_request: StockRequest, db: Session = Depends(get_db)):
    """""
    creates a stock and saves it to database
    """""

    return {
        "code":"success",
        "message":"created"
    }

