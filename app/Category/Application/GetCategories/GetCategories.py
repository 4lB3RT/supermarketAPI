from app.Category.Application.GetCategories.GetCategoriesResponse import GetCategoriesResponse
from app.Category.Domain.CategoryRepository import CategoryRepository

class GetCategories:
    def __init__(self, categoryRepository: CategoryRepository) -> None:
        self.__categoryRepository = categoryRepository
        pass
    
    def handle(self) -> GetCategoriesResponse:
        categories = self.__categoryRepository.find()
        
        return GetCategoriesResponse()



    