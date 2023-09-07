import requests
url="https://www.jmc.com.au/stock/search/"
headers = {
  'authority': 'www.jmc.com.au',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
}
car_count=629
per_page=10
total_page=round(car_count/per_page)
for page in range(1,total_page):
    payload=f'page={page}'
    response=requests.post(url=url,json=payload)
    with open (f"C:\\Users\\danie\\python_script\\post()_method\\supporting_files\\car{page}.html","w",encoding="utf-8")as file:
        file.write(response.text)
        