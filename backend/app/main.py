from fastapi import FastAPI
from app.routers import home

app = FastAPI(
    title = "Civica API",
    description = "AI- powered civic issue reporting platform",
    version = "1.0.0"
)

app.include_router(home.router)