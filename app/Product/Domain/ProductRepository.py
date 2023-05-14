from abc import abstractmethod
from app.Product.Domain.ProductCollection import ProductCollection

class ProductRepository():
    @abstractmethod
    def find() -> ProductCollection:
        pass