import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        blocks=response.xpath('//ol/li')
        source_url=response.url
        
        for block in blocks:
            book_name=block.xpath('.//h3/a/@title').get('')
            book_price=block.xpath('.//p[@class="price_color"]/text()').get('')
            stock_avalability=block.xpath('//p[@class="instock availability"]/text()').get()
            # breakpoint()
            yield{"source_url":source_url,"book_name":book_name,'book_price':book_price}
        next_page=response.xpath('//li[@class="next"]/a/@href').get()
        
        next_page=response.urljoin(next_page)
        yield scrapy.Request(next_page,callback=self.parse)
        
    

            
        
        
