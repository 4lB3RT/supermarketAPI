from app.Category.Domain.CategoryCollection import CategoryCollection

class GetCategoriesResponse:
    
    def __init__(self, categories: CategoryCollection) -> None:
        self.__categories = categories
        
    def categories(self) -> CategoryCollection:
        return self.__categories