import logging
from gpiozero import Button , LED , OutputDevice , Buzzer
from signal import pause
import os
import time


##############################################
#inizializzo il logging
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'
LOG_FILE = '/home/pi/log/db.log'
#RESULT_LOG_FILE = 'result.log'
LOG_FORMAT = '[%(asctime)s]  [%(levelname)s] %(message)s'
logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT, level=logging.DEBUG, filename=LOG_FILE)
logging.info('AVVIO')
#logging.basicConfig(filename="/home/pi/bin/db.log",level=logging.DEBUG)
#logging.basicConfig(format="%(asctime)s %(message)s")

###############################################


r1 = OutputDevice (14,active_high=True,initial_value=True)
r2 = OutputDevice (15,active_high=True,initial_value=True)
r3 = OutputDevice (17,active_high=True,initial_value=True)
r4 = OutputDevice (18,active_high=True,initial_value=True)



    r3.off()
    time.sleep(0.5)
    r3.on()
    logging.info("premuto b5")

