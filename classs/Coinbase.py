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


	def CoinBase(self):
		#BTC URLS
		btcAPIURL       = "https://www.coinbase.com/api/v2/prices/BTC-USD/spot?"
		btcHourAPIURL   = "https://www.coinbase.com/api/v2/prices/BTC-USD/historic?period=hour"

		#ETH URLS
		ethAPIURL       = "https://www.coinbase.com/api/v2/prices/ETH-USD/spot?"
		ethHourAPIURL   = "https://www.coinbase.com/api/v2/prices/ETH-USD/historic?period=hour"

		#LTC URLS
		ltcAPIURL       = "https://www.coinbase.com/api/v2/prices/LTC-USD/spot?"
		ltcHourAPIURL   = "https://www.coinbase.com/api/v2/prices/LTC-USD/historic?period=hour"

		currentBTC = s.get(btcAPIURL).json()['data']['amount']
		currentETH = s.get(ethAPIURL).json()['data']['amount']
		currentLTC = s.get(ltcAPIURL).json()['data']['amount']

		btcChangeAPI = s.get(btcHourAPIURL).json()['data']['prices']
		ethChangeAPI = s.get(ethHourAPIURL).json()['data']['prices']
		ltcChangeAPI = s.get(ltcHourAPIURL).json()['data']['prices']

		changeBTC    = float(btcChangeAPI[1]['price']) - float(btcChangeAPI[-1]['price'])
		changeETH    = float(ethChangeAPI[1]['price']) - float(ethChangeAPI[-1]['price'])
		changeLTC    = float(ltcChangeAPI[1]['price']) - float(ltcChangeAPI[-1]['price'])

		log("-------------------------------")
		log(Change.change("BTC", currentBTC, changeBTC))
		log(Change.change("ETH", currentETH, changeETH))
		log(Change.change("LTC", currentLTC, changeLTC))
		log("-------------------------------")

		for i in range(3600):
			returnLine()
			overWrite("%s%sSleeping... %d Seconds left%s" % (Style.BRIGHT,Fore.BLUE, 3600-i, Style.RESET_ALL), False)
			time.sleep(1)




