import scrapy


class JmcCarSpider(scrapy.Spider):
    name = "jmc_car"
    def start_requests(self):
        start_urls = "https://jmc.com.au"        
        yield scrapy.Request(start_urls,callback=self.parse)
        
    def parse(self, response):
        models=response.xpath('//select[@id="vehicleMake"]/option/text()').getall()
        search=response.xpath('//div[@class="nav-primary-wrapper "]//li/a[@title="Our Stock"]/@href').get('')   
        for model in models:
            if model == 'Audi (22)':
                brand=model.split(' ')[0]
                url = f'https://www.jmc.com.au/{search}'
                for i in range(1,4):
                    payload = f'vehicleTypeDemo=True&vehicleTypeUsed=True&page={i}&dealerLocation=0&vehicleMake={brand}&vehicleModel=&keywords=&dummyPriceFrom=&priceFrom=&dummyPriceTo=&priceTo=&budgetPeriod=week&depositAmount=&budgetAmount=&budgetDefaultValue=1000&orderBy=yearDesc&resultsPerPage=10'
                    headers = {
                        'authority': 'www.jmc.com.au',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                        'cache-control': 'max-age=0',
                        'content-type': 'application/x-www-form-urlencoded',
                        'origin': 'https://www.jmc.com.au',
                        'referer': 'https://www.jmc.com.au/',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
                        }
                    yield scrapy.Request(url=url,method='POST',headers=headers,body=payload,callback=self.parse_detail,dont_filter=True)
        
    
    
    def parse_detail(self,response):
        details=response.xpath('//a[@class="pure-button button-brand btn-base sl-btn-details"]/@href').getall()
        for detail in details:
            
            detail_url =response.urljoin(detail)
            yield scrapy.Request(detail_url,callback=self.parse_car)
            
    def parse_car(self,response):
        item={}
        item['source_url']=response.url
        item['car_name']=response.xpath('.//div/h3/text()').get('')
        item['car_price']=response.xpath('.//h4[@class="sl-heading-prices sl-price"]/text()').get('')
        car_info=response.xpath('.//div[@class="sd-specs-item"]/p[@class="sd-specs-text sd-specs-key"]/text()').getall()
        car_info_2=response.xpath('.//div[@class="sd-specs-item"]/p[@class="sd-specs-text sd-specs-value"]/text()').getall()
        item['dealer_name']=response.xpath('.//div[@id="locationName"]/text()').get('')
        item['dealer_address']=response.xpath('.//div[@class="pure-u-19-24 location-address location-address-text"]/text()').get('')
        item['dealer_no']=response.xpath('.//div[@class="pure-u-19-24 location-phone location-phone-text"]/a/text()').get('')
        item['dealer_mail']=response.xpath('.//div[@class="pure-u-19-24 location-email location-email-text"]/a/text()').get('')
        car_information=dict(zip(car_info,car_info_2))
        item['model_year']=car_information.get('Model Year','')
        item['Type']=car_information.get('Type','')
        item['Colour']=car_information.get('Colour','')
        item['Transmission']=car_information.get('Transmission','')
        item['Engine']=car_information.get('Engine','')
        item['Power']=car_information.get('Power','')
        item['GVM']=car_information.get('GVM','')
        item['GCM']=response.xpath('//div[@class="sd-specs-item"]/p[contains(text(),"GCM")]//following-sibling::p/text()').get('')
        item['Drive Type']=car_information.get('Drive Type','')
        item['Fuel System']=car_information.get('Fuel System','')
        item['Body']=car_information.get('Body','')
        item['VIN #']=response.xpath('//div[@class="sd-specs-item"]/p[contains(text(),"VIN")]//following-sibling::p/text()').get('')
        item['Reg #']=response.xpath('//div[@class="sd-specs-item"]/p[contains(text(),"Reg")]//following-sibling::p/text()').get('')
        item['Stock #']=response.xpath('//div[@class="sd-specs-item"]/p[contains(text(),"Stock")]//following-sibling::p/text()').get('')
        yield item
    
            
              
