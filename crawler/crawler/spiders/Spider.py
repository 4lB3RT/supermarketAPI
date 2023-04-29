import scrapy

import Category
import CategoryCollection

class Spider(scrapy.Spider):
    name = "spider"
    start_urls = [
        'https://www.dia.es/compra-online/#',
    ]

    def parse(self, response):
        categoryNames = response.css('.btn-main-category::text').getall()
        
        categoryList = []
       
        for categoryName in categoryNames:
            self.log(categoryName)
            category = Category(categoryName, "test")
            categoryList.append(category)
            
        self.log(categoryList)
            
           
       