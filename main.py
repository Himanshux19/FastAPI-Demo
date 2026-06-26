from fastapi import FastAPI, Depends
from models import Products
from database import session, engine
import database_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:3000"],allow_methods=["*"])

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# DataBase Initialization from list
# def init_db():
#     db = session()
#     count = db.query(database_models.Products).count
#     if count == 0:
#         for product in product_list:
#             db.add(database_models.Products(**product.model_dump()))
#         db.commit()

# init_db()

@app.get("/products")
def get_all_products(db : Session = Depends(get_db)):
    db_product = db.query(database_models.Products).all()
    return db_product

@app.get("/products/{id}")
def get_product_by_id(id :int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if db_product:
        return db_product
    return "No Such Product Found"

@app.post("/products")
def add_product(product : Products, db : Session = Depends(get_db)):
    db.add(database_models.Products(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(
    id: int,
    updated_product: Products,
    db: Session = Depends(get_db)
):
    db_product = db.query(database_models.Products).filter(
        database_models.Products.id == id
    ).first()

    if not db_product:
        return {"message": "No Such Product Found"}

    db_product.name = updated_product.name
    db_product.description = updated_product.description
    db_product.price = updated_product.price
    db_product.quantity = updated_product.quantity

    db.commit()
    db.refresh(db_product)

    return db_product

@app.delete("/products/{id}")
def delete_product(id : int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted Successfully!"
    return "No Such Product Found"