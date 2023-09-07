import requests
from parsel import Selector
url="https://www.jmc.com.au/stock/search/"
headers = {
  'authority': 'www.jmc.com.au',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://www.jmc.com.au',
  'referer': 'https://www.jmc.com.au/stock/search/',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
}
car_count=633
per_page=10
total_page=round(car_count/per_page)
for page in range(1,total_page+1):
    payload=f"page={page}"
    response=requests.post(url=url,headers=headers,data=payload)
    xpath_obj=Selector(response.text)
    # breakpoint()
    for list_xpath in xpath_obj.xpath('//div[@class="sl-items-wrapper"]/div[@class="stock-list-item"]'):
        title=list_xpath.x(".//h3/text( )").get()
        price=list_xpath.xpath('.//div/a[@class="sl-price-wrapper sl-price-now-wrapper disclaimer-content"]/h4/text()').get()
        link=list_xpath.xpath('.//div/a[@class="sl-heading-details-link"]/@href').get()
        link=f'https://www.jmc.com.au/{link}'
        with open ("car_details.txt","a",encoding="utf-8")as file:
            file.write(f"{title}\t{price}\t{link}\n")