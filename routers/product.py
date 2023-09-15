from fastapi import APIRouter, Path
from fastapi.params import Query

from models.product import Product

router = APIRouter()

products = [
    {
        "id":1,
        "name":"producto 1",
        "price":20,
        "stock": 10
    },

    {
        "id":2,
        "name":"producto 2",
        "price":30,
        "stock": 5
    }
]
@router.get('/productos')
def get_productos():
    return products

@router.get('/productos/{id}')
def get_producto(id:int= Path(gt=0)):
    return list (filter(lambda item: item['id'] == id, products))

@router.get('/productos/')
def get_poducts_by_stock(stock:int, price:float=Query(gt=0)):
    return list (filter(lambda item: item['stock'] == stock and item['price']== price, products))

@router.post('/productos')
def create_products(product:Product):
    products.append(product)
    return products

@router.put('/productos/{id}')
def update(id:int, product: Product):
    for index, item in enumerate(products):
        if item['id'] == id:
            products[index]['name'] = product.name
            products[index]['stock'] = product.stock
            products[index]['price'] = product.price
    return products

@router.delete("/productos/{id}")
def delete(id:int):
    for item in products:
        if item['id'] == id:
            products.remove(item)
    return products
