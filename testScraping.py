from bs4 import BeautifulSoup
from urllib.request import urlopen

redditFile = urlopen("http://www.opendatalabs.co.in")
redditHtml = redditFile.read()
redditFile.close()

soup = BeautifulSoup(redditHtml, "lxml")
#soup = BeautifulSoup(redditHtml, "html5lib")
print(soup.title.string)
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))
