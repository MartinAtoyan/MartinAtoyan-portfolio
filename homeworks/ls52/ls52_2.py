from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
]

class User(BaseModel):
    name: str

class Product(BaseModel):
    name: str
    price: float

@app.get("/user")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id:int):
    # user = None
    # for u in users:
    #     if u["id"] == user_id:
    #         user = u
    #         break
    # if not user:
    # return user

    for user in users:
        if user["id"] == user_id:
            return user
        
    raise HTTPException(status_code=404, detail="User not found")
            

@app.put("/users/{user_id}")
def create_user(user: User):
    new_id = max(user["id"] for user in users)
    new_user = {"id": new_id + 1, "name": user["name"]}
    users.append(new_user)

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    for u in users:
        if u["id"] == user_id:
            u["name"] = user["name"]
            u["id"] = user["id"]
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)

@app.get("/products")
def get_products():
    return products

@app.get("/product/{product_id}")
def get_product(product_id: int):
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break
    if not product:
        raise HTTPException(status_code=404, detail="Not found product")
    return product

@app.post("/products", status_code=201)
def create_product(product: Product):
    new_id = max(prod["id"] for prod in products)
    new_product = {"id": new_id + 1, "name":product["name"], "price":product["price"]}
    products.append(new_product)

@app.put("/products/{product_id}")
def update_product(product: Product, product_id: int):
    for prod in products:
        if prod["id"] == product_id:
            prod["name"] = product["name"]
            prod["price"] = product["price"]
            return prod
        raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(prod_id: int):
    for prod in products:
        if prod["id"] == prod_id:
            products.remove(prod)
