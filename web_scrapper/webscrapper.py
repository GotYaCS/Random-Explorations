import urllib.request
from bs4 import BeautifulSoup

ews = "https://it.engineering.illinois.edu/ews"
page = urllib.request.urlopen(ews)
soup = BeautifulSoup(page,features="html.parser")
# print(soup.prettify())
labs=soup.find(id="DCL_L426",class_="lab")


    

print(labs)