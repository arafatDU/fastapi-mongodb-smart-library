from fastapi import FastAPI
import uvicorn
import os
from app.database import init_db
from app.users.routes import router as users_router
from app.books.routes import router as books_router
from app.loans.routes import router as loans_router
from contextlib import asynccontextmanager

DEBUG = os.environ.get("DEBUG", "").strip().lower() in {"1", "true", "on", "yes"}


# Use lifespan to handle startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()  # Startup action
    yield


app = FastAPI(lifespan=lifespan)


# Include routers for different modules
app.include_router(users_router, prefix="/api/users", tags=["Users"])
app.include_router(books_router, prefix="/api/books", tags=["Books"])
app.include_router(loans_router, prefix="/api/loans", tags=["Loans"])

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
