from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {
        "message":"welcome to Civica Backend"
    }

@router.get("/about")
def about():
    return {
        "project":"Civica",
        "version":"1.0",
        "developer":"Mohd Maaz Khan"
    }

@router.get("/health")
def health():
    return{
        "status": "Healthy",
        "server": "Running",
        "database": "Not Connected Yet"
    }