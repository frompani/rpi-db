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
print "In/Out Board"
last_status=None
os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=63&switchcmd=Off"')

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
    result = bluetooth.lookup_name('22:22:D6:8C:E9:17', timeout=2)
    if (last_status !=result):
    	if (result != None):
        	print "RF a casa"
		logging.info("RF a casa!")
                last_status="Rf"
		os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=63&switchcmd=On"')
    	else:
        	print "RF fuori"
                logging.info("RF uscito!")
                last_status=None
                os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=63&switchcmd=Off"')

    time.sleep(5)

