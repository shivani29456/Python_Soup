import requests
import urllib.request
from bs4 import BeautifulSoup

A=[]
url = ("https://wiki.metakgp.org/w/Special:ContributionScores")
r=requests.get(url)
html_content=r.content
soup=BeautifulSoup(html_content,"html.parser")

all_tables=soup.findAll('table')
right_table=soup.find('table',class_='wikitable contributionscores plainlinks sortable jquery-tablesorter')
for tr in soup.find_all("tr"):
    try:



        td = tr.findAll("td")

        A.append(td[4].find(text=True))

    except Exception as e:
        print(e,tr)

print(A[0:3])




