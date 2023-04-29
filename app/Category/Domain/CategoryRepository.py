from abc import abstractmethod
from app.Category.Domain.CategoryCollection import CategoryCollection

class CategoryRepository():
    @abstractmethod
    def find() -> CategoryCollection:
        pass