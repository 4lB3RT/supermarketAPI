from app.Category.Domain import Category

class CategoryCollection:
    def __init__(self, items: list[Category]):
        self.__items = items
        
    def items(self) -> list: 
        return self.__items
    
    def add(self, category: Category) -> None:
        self.__items.append(category)