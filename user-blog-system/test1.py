from fastapi import FastAPI

myapp = FastAPI()

@myapp.get("/")

def message():

    return {"message":"hello world"}

