from fastapi import FastAPI
from app.database import init_db
import uvicorn
import os
from contextlib import asynccontextmanager

DEBUG = os.environ.get("DEBUG", "").strip().lower() in {"1", "true", "on", "yes"}

# Use lifespan to handle startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()  # Startup action
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

def main():
    try:
        uvicorn.run("app.main:app", host="0.0.0.0", port=3001, reload=DEBUG)
    except KeyboardInterrupt:
        print("Server stopped")

if __name__ == "__main__":
    main()
