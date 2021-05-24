import uvicorn

from src.api.v1_0 import app
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run("start_app:app", host="0.0.0.0", port=8000, reload=True)

