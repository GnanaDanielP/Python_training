import requests
from parsel import Selector
url="https://www.autotrader.com/cars-for-sale/all-cars/moody-al?zip=35004"
response=requests.get(url=url)
xpath_obj=Selector(text=response.text)
details = xpath_obj.xpath('//div[@data-cmp="itemCard"]//div[@class="display-flex justify-content-between"]/a[@data-cmp="link"]')
for detail in details:
  link = detail.xpath('./@href').get('')
  link=f'https://www.autotrader.com{link}'
  # breakpoint()
  car_response=requests.get(link)
  detail_xpath_obj=Selector(text=car_response.text)
  
  name=detail_xpath_obj.xpath('//h1/text()').get('') 
  price=detail_xpath_obj.xpath('//div[@data-cmp="pricing"]/span[@data-cmp="firstPrice"]/text()').get('')
  engine=detail_xpath_obj.xpath('//div[@aria-label="ENGINE_DESCRIPTION"]/parent::div/following-sibling::div/text()').get('')
  mileage=detail_xpath_obj.xpath('//div[@aria-label="MILEAGE"]/parent::div/following-sibling::div/text()').get('')
  fuel=detail_xpath_obj.xpath('//div[@aria-label="MPG"]/parent::div/following-sibling::div/text()').get('')
  color=detail_xpath_obj.xpath('//div[@data-cmp="colorSwatch"]/parent::div/following-sibling::div/text()').get('')
  transmission=detail_xpath_obj.xpath('//div[@aria-label="TRANSMISSION"]/parent::div/following-sibling::div/text()').get('')
  drive_type=detail_xpath_obj.xpath('//div[@aria-label="DRIVE TYPE"]/parent::div/following-sibling::div/text()').get('')
  bed_length=detail_xpath_obj.xpath('//div[@aria-label="BED LENGTH"]/parent::div/following-sibling::div/text()').get('') 
  with open (r"C:\Users\danie\python_script\trader\auto_trader_output.txt","a+",encoding="utf-8")as file:
    file.write(f'{link}\t{name}\t{price}\t{engine}\t{mileage}\t{fuel}\t{color}\t{transmission}\t{drive_type}\t{bed_length}\n')
  
  
  

  
