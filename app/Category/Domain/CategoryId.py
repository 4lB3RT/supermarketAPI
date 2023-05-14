from app.Category.Domain import categoryId

class CategoryIdCollection:
    def __init__(self, items: list[categoryId]):
        self.__items = items
        
    def items(self) -> list: 
        return self.__items