from app.Category.Domain import Category
from app.Product.Domain.Product import Product

class ProductCollection:
    def __init__(self, items: list[Product]):
        self.__items = items
        
    def items(self) -> list: 
        return self.__items
    
    def add(self, product: Product) -> None:
        self.__items.append(product)