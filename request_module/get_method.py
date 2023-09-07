import requests
url=("https://en.wikipedia.org/wiki/Vairamuthu")


# breakpoint()

headers={
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authority': 'en.m.wikipedia.org',
    
}
response=requests.get(url,headers=headers)
# breakpoint()
with open (r"C:\Users\danie\OneDrive\Documents\request_module\supporting_file\vairamuthu.html","w",encoding="utf-8") as file:
    file.write(str(response.text))

print(response.status_code)
print(response.headers)
print(response.request.headers)
print(response.url)