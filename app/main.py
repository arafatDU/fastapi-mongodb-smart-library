from fastapi import FastAPI
import uvicorn
import sys
import os


DEBUG = os.environ.get("DEBUG", "").strip().lower() in {"1", "true", "on", "yes"} 
 
app = FastAPI()
 

@app.get("/")
def read_root():
    return {"Hello": "World"} 
 
  
def main():
  try:
    uvicorn.run("main:app", host="0.0.0.0", port=3001, reload=DEBUG)
  except KeyboardInterrupt:
    print("Server stopped")
    pass
  
if __name__ == "__main__":
  main()