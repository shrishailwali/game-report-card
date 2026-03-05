import os
from fastapi import APIRouter, UploadFile, File
from app.services.video_processor import process_video

router = APIRouter()

UPLOAD_FOLDER = "uploads"

@router.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = process_video(file_path)

    return {
        "message": "Video processed successfully",
        "analysis": result
    }
