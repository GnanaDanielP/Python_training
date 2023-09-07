import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

        
    start_urls =[ "https://quotes.toscrape.com/"]


    def parse(self, response): 
        
        blocks= response.xpath('//div[@class="quote"]')
        source_url=response.url
        for block in blocks:
            quote=block.xpath('./span/text()').get('') 
            author=block.xpath('./span/small[@class="author"]/text()').get('')
        
                                               
            
            # breakpoint()
            yield{'source_url':source_url,'quotes':quote,'authors':author}
        next_page=response.xpath('//li[@class="next"]/a/@href').get()
        # breakpoint()
        
        if next_page:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(url=next_page,callback=self.parse)
        
        tags=response.xpath('//span[@class="tag-item"]/a/@href').get('')
        if tags:
            tags=response.urljoin(tags)
            yield scrapy.Request(url=tags,callback=self.parse)
            
            
            
