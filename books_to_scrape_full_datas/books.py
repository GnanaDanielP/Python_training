import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        blocks=response.xpath('//ol/li')
        source_url=response.url
        
        for block in blocks:
            book_url=block.xpath('.//div[@class="image_container"]/a/@href').get('')
            book_url=response.urljoin(book_url)
            book_name=block.xpath('.//h3/a/@title').get('')
            book_price=block.xpath('.//p[@class="price_color"]/text()').get('')
            detail_url=block.xpath('.//div[@class="image_container"]/a/@href').get('')
            detail_url=response.urljoin(detail_url)
            yield scrapy.Request(url=detail_url, callback=self.parse_detail,dont_filter=True,cb_kwargs={"source_url":source_url,"book_name":book_name,'book_price':book_price,'book_url':book_url})
            
            
        next_page=response.xpath('//li[@class="next"]/a/@href').get('')
        if next_page:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
    
        
        
    def parse_detail(self, response,source_url,book_name,book_price,book_url):
        detail_pages=response.xpath('//table[@class="table table-striped"]')
        
        for detail_page in detail_pages:
            product_information=detail_page.xpath('.//th/text()').getall()
            info_details=detail_page.xpath('.//td/text()').getall()
            description=detail_page.xpath('//div[@id="product_description"]/following-sibling::p/text()').get()
            book_details = dict(zip(product_information,info_details))
            item = {'source_url':source_url,'book_url':book_url,'book_name':book_name,'book_price':book_price,'product_description':description}
            item = item|book_details
            yield item
            
    

            
        
        
