from bs4 import BeautifulSoup
from urllib.request import urlopen

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w+")

for inputUrl in inputFile.readlines():
    print(inputUrl)
    redditFile = urlopen(inputUrl)
    redditHtml = redditFile.read()
    redditFile.close()

    soup = BeautifulSoup(redditHtml, "lxml")
    #soup = BeautifulSoup(redditHtml, "html5lib")
    print(soup.title.string)
    redditAll = soup.find_all("a")
    for links in soup.find_all('a'):
        print (links.get('href'))
        outputFile.writelines(links.get('href'))
        outputFile.writelines("\n")

inputFile.close()
outputFile.close()