from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/user")
def hello_world():
    return "Hello user"

@app.get("/say-hello/{name}")
def say_hello(name: str):
    return f"Hello {name}"

