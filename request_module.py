import requests
URL=requests.get("https://en.wikipedia.org/wiki/MS_Dhoni")
print(URL.status_code)
with open("C:\Daniel\Supporting_files\dhoni.html","w",encoding='utf-8-sig')as file:
    file.write(URL.text)
         