from fastapi import FastAPI
from app.routes.video_routes import router as video_router

app = FastAPI(title="AI Game Analytics")

app.include_router(video_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "Backend running"}
