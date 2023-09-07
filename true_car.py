import requests
url="https://www.truecar.com/used-cars-for-sale/listings/location-nashville-tn/"
headers = {
  'authority': 'www.jmc.com.au',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
  'x-requested-with': 'XMLHttpRequest'
}
response=requests.get(url=url,headers=headers)
with open ("true_car.html","w",encoding="utf-8")as file:file.write(response.text)
