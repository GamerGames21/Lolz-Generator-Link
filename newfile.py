import random, webbrowser, requests
from bs4 import BeautifulSoup

while 0 == 0:
	startlink = "https://lolz.guru/threads/"
	number = random.randint(1,4000000)
	link = startlink + str(number)
	webbrowser.open(link, new=0)
	input("Готово")