from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello im Alyona from Russia! IVT 1.2"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
