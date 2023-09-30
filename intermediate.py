import requests
from bs4 import BeautifulSoup
array=[]
url = 'https://www.tradingview.com/markets/stocks-india/market-movers-large-cap/'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
trs=soup.find_all("tr",class_="row-RdUXZpkv")
for tr in trs:
    tds=tr.find_all("td")
    name=tds[0].find("sup").text
    price=tds[2].text
    array.append([name,price])
print(array)
    
