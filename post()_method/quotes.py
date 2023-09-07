import requests
from parsel import Selector
url=["http://quotes.toscrape.com/",
    "http://quotes.toscrape.com/page/2/",
    "http://quotes.toscrape.com/page/3/"
]
headers = {
  'authority': 'www.jmc.com.au',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
}
for page in url:
    response=requests.get(url=page,headers=headers)
    xpath_obj=Selector(response.text)
    for list_obj in xpath_obj.xpath('//div[@class="quote"]'):
        quote=list_obj.xpath('./span[@class="text"]/text()').get('')
        author=list_obj.xpath("./span/small/text()").get()
        tags=list_obj.xpath('.//a[@class="tag"]/@href').get()
        with open ("testing.html",'a')as file:
            file.write(f'{quote}\t,{author}\t,{tags}\n')
        
