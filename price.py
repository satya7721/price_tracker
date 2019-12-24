import requests
from bs4 import BeautifulSoup

#amazon module:

url="https://www.amazon.in/s?k="
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#input product and validation:
user_input=raw_input("enter pro:")
user_input=user_input.replace(" ","+")


#requesting :
req=requests.get(url+user_input,headers=headers)

#soup operation:

soup=BeautifulSoup(req.content,'html.parser')

span =soup.find_all('span', class_="a-price-whole")
price=[]
for sp in span:
    sk=sp.text.replace(',','').replace('.','')
    price.append(int(sk))



for sp in span:
    sk=sp.text.replace(',','').replace('.','')
    if(min(price)==int(sk)):
        print(sp)
