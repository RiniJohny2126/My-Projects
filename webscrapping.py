import requests
from bs4 import BeautifulSoup
web_url= "https://quotes.toscrape.com/"
res= requests.get(web_url)
soup= BeautifulSoup(res.text,'lxml')
quotes=soup.find_all("div",{"class":"quote"})
for i in quotes:
    title_element= i.find("a")
    titlename=title_element.text
    titlelink=title_element["href"]
    print(titlename,titlelink)
 