from fastapi import FastAPI

from .routers import products, upload

app = FastAPI()

app.include_router(products.router)
app.include_router(upload.router)

@app.get("/")
async def root():
    return {"message": "Hello Cosmocode!"}