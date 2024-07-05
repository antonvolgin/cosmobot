from fastapi import FastAPI

from .routers import users, products, upload

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(upload.router)

@app.get("/")
async def root():
    return {"message": "Hello Cosmocode!"}