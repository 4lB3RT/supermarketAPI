from app.Category.Domain.CategoryId import CategoryIdCollection


class Product:
    def __init__(
        self,
        name: str,
        price: float,
        categoryIds: CategoryIdCollection,
        supermarket: str
    ) -> None:
        self.__name = name
        self.__price = price
        self.__categoryIds = categoryIds
        self.__supermarket = supermarket
        
    def name(self) -> str:
        return self.__name
    
    def price(self) -> float:
        return self.__price
    
    def categoryIds(self) -> CategoryIdCollection:
        return self.__categoryIds
    
    def supermarket(self) -> str:
        return self.__supermarket