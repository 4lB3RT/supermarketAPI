from app.Category.Domain import CategoryId
from app.Product.Domain import ProductCollection


class Category:
    def __init__(
        self,
        id: CategoryId| None,
        name: str,
        published: bool,
        url: str,
        products: ProductCollection|None
        ) ->  None :
        self.__id = id
        self.__name = name
        self.__published = published
        self.__url = url
        self.__products = products
        
    def id(self) -> CategoryId|None:
        return self.__id
    
    def name(self) -> str:
        return self.__name
    
    def published(self) -> bool:
        return self.__published
    
    def url(self) -> str:
        return self.__url

    def products(self) -> ProductCollection|None:
        return self.__products