import requests
from bs4 import BeautifulSoup
from lxml import html

pNo = 310
while pNo <= 310:
    page = requests.get("URL/all/" + str(pNo))
    webpage = html.fromstring(page.content)
    tiles = webpage.xpath('//a/@href')
    tNo = 40
    while tNo <= 63:
        try:
            game = requests.get("URL" + str(tiles[tNo]))
            soup = BeautifulSoup(game.content, 'html.parser')
            swf = soup.findAll('meta')
            l = str(swf[11])
            l = l.split("\"")
            name = l[1].split("/")
            name = name[-1]
            final = requests.get("URL" + str(l[1]))
            myGame = open('F:\WebScrape\\' + name, "wb")
            myGame.write(final.content)
            print("Page: ", pNo, "Game: ", tNo - 39, "/24 DONE! ", name)

        except:
            print(" !! ERROR COULD NOT SAVE ", "Page: ", pNo, "Game: ", tNo - 39, "/24 ")

        finally:
            tNo += 1
    pNo += 1

#150
