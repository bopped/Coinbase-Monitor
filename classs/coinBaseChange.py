import os
from colorama import *

if os.name == 'nt':
	init()

class Change:

	def change(self, Crypto, currentPrice, hourlyChange):
		if hourlyChange < 0.0:
			#return True
			return "%s Current Price: %10s | Hourly Change: %s%s%f%s" % (Crypto, currentPrice, Style.BRIGHT, Fore.RED, hourlyChange, Style.RESET_ALL)

		if hourlyChange > 0.0:
			return "%s Current Price: %10s | Hourly Change: %s%s%f%s" % (Crypto, currentPrice, Style.BRIGHT, Fore.GREEN, hourlyChange, Style.RESET_ALL)

