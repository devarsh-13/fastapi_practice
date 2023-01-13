from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/async-example")
async def example_async_endpoint():
    await asyncio.sleep(1)
    return {"message": "Hello, async world!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    await asyncio.sleep(0.5)
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: dict):
    await asyncio.sleep(1)
    return {"item": item}