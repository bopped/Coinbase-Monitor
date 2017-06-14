import time, json, requests, random, threading, os
from sys import stdout
from colorama import *

#Needed on Windows
if os.name == 'nt':
	init()

#logger init
from classs.logger import logger
log        = logger().log
overWrite  = logger().overwriteLine
returnLine = logger().returnLine
s          = requests.Session()

from classs.coinBaseChange import Change
Change = Change()



class Monitor:


	def CoinBase(self, config):
		Warned      = False
		Cryptos     = config['Monitor']['Name']
		sleepTime   = config['Monitor']['Sleep']

		while True:

			log("--------------------------------------------------------------")

			for x in range(len(Cryptos)):
				Crypto = Cryptos[x].upper()

				if len(Crypto) != 3:
					if not Warned:
						log("One of the cryptos in your config is wrong, scraping properly setup ones anyways!",'info')
						Warned = True
					continue

				currentPriceAPI    = "https://www.coinbase.com/api/v2/prices/%s-USD/spot"                  % (Crypto)
				HourAPIURL         = "https://www.coinbase.com/api/v2/prices/%s-USD/historic?period=hour"  % (Crypto)

				currentPrice       = s.get(currentPriceAPI).json()['data']['amount']
				hourChangeAPI      = s.get(HourAPIURL).json()['data']['prices']
				changeCrypto       = float(hourChangeAPI[1]['price']) - float(hourChangeAPI[-1]['price'])

				log(Change.change(Crypto, currentPrice, changeCrypto))

			log("--------------------------------------------------------------")

			for i in range(sleepTime):
				returnLine()
				overWrite("%s%sSleeping... %d Seconds left%s" % (Style.BRIGHT,Fore.BLUE, sleepTime-i, Style.RESET_ALL), False)
				time.sleep(1)

			overWrite("", True)
			log("%s%sRe-Scraping!%s" % (Style.BRIGHT,Fore.BLUE, Style.RESET_ALL))



