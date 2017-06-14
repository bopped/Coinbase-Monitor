import os, json 
from colorama import *

#Needed on Windows
if os.name == 'nt':
	init()

from classs.logger import logger
log     = logger().log

from classs.Coinbase import Monitor

coinbaseMonitor = Monitor()



if not os.path.exists("config.json"):
	log("%sConfig.json not Found!!!"  %  (Fore.RED))
	exit()

with open('config.json') as json_data_file:
	config = json.load(json_data_file)

log("-------------------------------")
log("%s%sConfiguration loaded.%s" % (Style.BRIGHT, Fore.GREEN, Style.RESET_ALL))
log("%s%sMade by Simmy.%s" % (Style.BRIGHT, Fore.RED, Style.RESET_ALL))
log("-------------------------------")
log("%s%sCoinBase Monitor Started!%s" % (Style.BRIGHT, Fore.GREEN, Style.RESET_ALL))


coinbaseMonitor.CoinBase(config)