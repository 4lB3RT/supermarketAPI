class Category:
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    def name(self) -> str:
        return self.__name
    
    def description(self) -> str:
        return self.__description
    