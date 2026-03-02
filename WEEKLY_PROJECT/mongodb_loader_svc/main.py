from fastapi import FastAPI
from grid_fs_orchestrator import GridFSOrchestrator
import uvicorn



my_router = GridFSOrchestrator().router

app = FastAPI()
app.include_router(my_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8200)