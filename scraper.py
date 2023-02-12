import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.1mg.com/all-diseases")

soup = BeautifulSoup(req.content, "html.parser")

all_links = list()

anchors = soup.find_all('a')


for link in anchors:
    if(link.get('href') != '#'):
        linktext = "https://www.1mg.com/all-diseases" +link.get('href')
        all_links.append(link)
        r = requests.get(linktext)
        soup2 = BeautifulSoup(r.content, "html.parser")
        paras = soup2.find_all('p')
        print(paras)
