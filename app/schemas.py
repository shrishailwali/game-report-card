from pydantic import BaseModel

class VideoCreate(BaseModel):
    filename: str

class VideoRead(BaseModel):
    id: int
    filename: str
    status: str

    class Config:
        orm_mode = True
