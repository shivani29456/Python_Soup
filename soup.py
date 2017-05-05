import requests
import urllib.request
from bs4 import BeautifulSoup


url = ("https://wiki.metakgp.org/w/Special:ContributionScores")
r=requests.get(url)
html_content=r.content
soup=BeautifulSoup(html_content,"html.parser")
for tr in soup.find_all("tr"):
    try:
        td = tr.findAll("td")
        print(td)
    except Exception as e:
        print(e,tr)






