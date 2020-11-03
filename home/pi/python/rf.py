#!/usr/bin/python

import bluetooth
import time
import logging
import os

##############################################
#inizializzo il logging
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'
LOG_FILE = '/home/pi/log/presence.log'
LOG_FORMAT = '[%(asctime)s]  [%(levelname)s] %(message)s'
logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT, level=logging.DEBUG, filename=LOG_FILE)
logging.info('AVVIO')
###############################################
DEVICES=['22:22:D6:8C:E9:17','F4:60:E2:21:9E:4F']
NAMES=['rf','chia']

last_status=None

while True:
	for device in DEVICES:
			result = bluetooth.lookup_name(device, timeout=2)
		print(result)
		if (result != None):
		  os.system('echo "1">p.txt')
		else:
		  os.system('echo "0">p.txt')
		time.sleep(1)



