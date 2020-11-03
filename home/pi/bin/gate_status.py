import logging
from gpiozero import Button , LED , OutputDevice , Buzzer
from signal import pause
import os
import time
from subprocess import check_call

gs=False

##############################################
#inizializzo il logging
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'
LOG_FILE = '/home/pi/log/db.log'
#RESULT_LOG_FILE = 'result.log'
LOG_FORMAT = '[%(asctime)s]  [%(levelname)s] %(message)s'
logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT, level=logging.DEBUG, filename=LOG_FILE)
logging.info('AVVIO')

##############################################
gate_status = Button(4,pull_up=True,bounce_time=0.2,hold_time=5)
##############################################\
#button pressed = cancello chiuso 
#button released = cancello aperto 
#prima esecuzione
if gate_status.is_pressed:
  print("cancello chiuso")
  logging.info("Cancello chiuso")
else:
  print("cancello aperto")
  logging.info("Cancello aperto")

#ciclo infinito
while True:
     if gate_status.is_pressed:
       if gs == False:
          print("cancello chiuso")
          gs = True
          os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=110&switchcmd=Off"') 	
          logging.info("Cancello chiuso")
     else:

       if gs == True:
          print("cancello aperto ")
          gs = False
          os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=110&switchcmd=On"')
          logging.info("Cancello aperto")
     time.sleep(30)
	
