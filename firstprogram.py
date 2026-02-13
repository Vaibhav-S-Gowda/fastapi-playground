# Import FastAPI class
from fastapi import FastAPI

# Create FastAPI app object
app = FastAPI()

# Root endpoint (homepage)
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Path parameter example
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
