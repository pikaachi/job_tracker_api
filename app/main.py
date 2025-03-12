import logging
from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.database import engine
from app import models

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Tracker API!"}
