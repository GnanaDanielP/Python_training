import requests
url='https://lesotholii.org/judgments/'
headers = {
        'authority': 'www.jmc.com.au',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.jmc.com.au',
        'referer': 'https://www.jmc.com.au/stock/search/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
        'x-requested-with': 'XMLHttpRequest'
}
response=requests.get(url=url,headers=headers)
with open ("sample.pdf","w",encoding="utf-8")as file :
    file.write(response.text)


        


 