import requests
from bs4 import BeautifulSoup
from lxml import html
import re

pNo = 1
while pNo <= 10:
    cf = 0
    page = requests.get("https://www.comdotgame.com/adult/" + str(pNo))
    webpage = html.fromstring(page.content)
    ntiles = webpage.xpath('//a/@href')
    start_string = 'https://www.comdotgame.com/play/'
    tiles = [x for x in ntiles if x.startswith(start_string)]

    if tiles == []:
        #print("CloudFare Error Page: ", pNo)
        cf += 1
        continue

    else:
        try:
            tNo = 0
            while tNo <= 25:
                #tiles = tiles[35:61] #list of links to the games on a page
                game = requests.get(tiles[35 + tNo])
                if game.status_code == 525:
                    #print("Cloudfare Error Game Page: ", print(tiles[35+tNo]))
                    cf +=1
                    continue

                else:
                    soup = BeautifulSoup(game.content, 'html.parser')
                    title = soup.find('title')
                    gamePage = str(soup)

                    gptr = gamePage.find("var filename = \"https://comdotcdn.com/games/files/")

                    glink_raw = gamePage[gptr+14:gptr+116]

                    glink = str(re.findall('"([^"]*)"', glink_raw)) #final game link

                    final = requests.get("https://echo.comdotgame.com/4x90xhl3k0" + str(glink[23:-2]), stream=True) #requests the final file

                    if len(glink) > 35:

                        new_name = ''
                        for character in title.string:
                            if character.isalnum():
                                new_name += character

                        myGame = open('G:\WebScrape2\\' + str(new_name) + '.swf', "wb") #saves the file
                        myGame.write(final.content)

                        print("Done! ", "Page: ", pNo, "/184 ", "Game: ", tNo, "/25 ", new_name)

                    else:
                        print("Empty Link!!!!!!!!!!!!!!!!!\n")

                    tNo += 1
        except:
            print("\n\n !!ERROR!! ", "Page: ", pNo, "Game: ", tNo, new_name, "\n\n")
        finally:
            tNo +=1

    print("Cloudfare Errors: ", cf)
    pNo += 1
#59

#page two needs 70 + 1
#Manual for the first 4 pages then?
#7 8 9 10 11 11 11 11