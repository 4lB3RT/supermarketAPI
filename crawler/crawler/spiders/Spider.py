import scrapy
from bs4 import BeautifulSoup

class Spider(scrapy.Spider):
    name = "spider"
    start_urls = [
        'https://www.dia.es/compra-online/#',
    ]

    def parse(self, response) -> None:
        self.__frescos(response=response)
        
    def __frescos(self, response) -> list:
        frescosName = response.css('.nav-submenu > li:nth-child(3) .btn-main-category::text').get()
        subCategoryNames = response.css('.nav-submenu > li:nth-child(3) .child-menu-frescos > .child-menu-container').getall()
        subCategoryNamesChild = response.css('.child-menu .child-menu-container li:first-child .grandchild-menu li span::text').getall()
        
        self.log(subCategoryNames)
        pass
