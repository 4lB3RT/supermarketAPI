class CategoryId:
    def __init__(self, value: int) -> None:
        self.__value = value
        
    def value(self) -> int:
        return self.__value