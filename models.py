from pydantic import BaseModel

class Products(BaseModel):
    id : int
    name : str
    price : float
    description : str
    quantity : int
