from grid_fs_storage import *
from fastapi import APIRouter, UploadFile, File
from typing import Annotated
import uuid


class GridFSOrchestrator:

    def __init__(self):
        self.router = APIRouter()
        self.fs = GridFSStorage().get_grid_fs()
        self.router.post("/set_image")(self.set_image_data)

    async def set_image_data(self, file: UploadFile = File(...)):
        b = await file.read()
        file_id = self.fs.put(b)
        return {"file_id": str(file_id)}
