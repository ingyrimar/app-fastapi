from fastapi import FastAPI
from routers.product import router as product_router

app = FastAPI()
app.include_router(product_router)

@app.get('/')
def mensaje():
    return "hola mundo"
