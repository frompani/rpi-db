import logging
from gpiozero import Button , LED , OutputDevice , Buzzer
from signal import pause
import os
import time
from subprocess import check_call

# cattura immagine fatto con domoticz M
##da provare cattura foto da cam1 
#http://192.168.10.91/fifo_command.php?cmd=still
#video 5 s prima e 55 s dopo
#http://192.168.10.91/fifo_command.php?cmd=record%20on%205%2055

gs=False

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
###definisco in-out

r1 = OutputDevice (14,active_high=True,initial_value=True)
r2 = OutputDevice (15,active_high=True,initial_value=True)
r3 = OutputDevice (17,active_high=True,initial_value=True)
r4 = OutputDevice (18,active_high=True,initial_value=True)

bz1 = Buzzer(22) 
bz2 = Buzzer(27)

db1 = Button(5,pull_up=True,hold_time=0.2)
db2 = Button(6,pull_up=True,hold_time=0.2)
bt_p1_a = Button(13,pull_up=True,hold_time=0.3)
bt_p1_b = Button(19,pull_up=True,hold_time=0.3)
bt_pt_a = Button(26,pull_up=True,bounce_time=0.5,hold_time=5)
#bt_pt_b = Button(26,pull_up=True,bounce_time=0.5,hold_time=5)
#gate_status = Button(4,pull_up=True,bounce_time=0.2,hold_time=5)
##############################################
def shutdown():
    check_call(['sudo', 'halt'])
##############################################
##2018-09-20_sostituito con chiamata a domoticz
##    os.system('ssh pi@192.168.10.181 "sh /home/pi/bin/doorbell/suona_campanello_grande.sh &"&')
##    os.system('cat /home/pi/bin/mail_cancello_grande.txt|sendmail frompani@gmail.com')

def ring_db1():
    print("campanello cancello grande")
    suono1() 
    os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=48&switchcmd=On"')
    print("aspetto")
    logging.info("suonato campanello cancello grande")
##############################################
def ring_db2():
    suono2()
    print("campanello cancello piccolo")
    os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=49&switchcmd=On"')
    print("aspetto")
    logging.info("suonato campanello cancello piccolo")
##############################################
def push_bt_p1_a():
    print("Premuto bt_p1_a!")
    r1.off()
    time.sleep(0.5)
    r1.on()
#   os.system('cat /home/pi/bin/mail.txt|sendmail frompani@gmail.com')
    logging.info("premuto bt_p1_a")
##############################################
#def rel_b3():
#    print ("Rilasciato b3!")
#    logging.info("Rilasciato b3")
##############################################
def push_bt_p1_b():
    print("premuto bt_p1_b!")
    r3.off()
    time.sleep(0.5)
    r3.on()
    logging.info("premuto bt_p1_b")
##############################################
def push_bt_pt_a():
    print("Premuto bt_pt_a!")
    r3.off()
    time.sleep(0.5)
    r3.on()
    logging.info("premuto bt_pt_a")
##############################################
#def rel_b5():
#        print ("Rilasciato b5!")
#        logging.info("Rilasciato b5")
##############################################
def suono2():
 x=1
 while x<5:
  bz2.on()
  time.sleep(0.2)
  bz2.off()
  time.sleep(0.1)
  x=x+1
 return
def suono1():
 x=1
 while x<5:
  bz1.on()
  time.sleep(0.2)
  bz1.off()
  time.sleep(0.1)
  x=x+1
 return
############################################## 
def gate_close():
    print("cancello chiuso")
#    os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=49&switchcmd=On"')
    logging.info("Cancello chiuso")
##############################################
def gate_open():
    print("cancello aperto")
#    os.system('curl -s "http://192.168.10.181:8888/json.htm?type=command&param=switchlight&idx=49&switchcmd=On"')
    logging.info("Cancello aperto")
###############################################
db1.when_held = ring_db1
db2.when_held = ring_db2
bt_p1_a.when_held = push_bt_p1_a
bt_p1_b.when_held = push_bt_p1_b
bt_pt_a.when_pressed = push_bt_pt_a
bt_pt_a.when_held = shutdown
##button.when_released = say_goodbye
#gate_status.when_held = gate_close
#gate_status.when_released = gate_open

#while True:
#    if gate_status.is_pressed:
#       if gs == False: 
#          print("cancello chiuso")
#          gs = True
#          logging.info("Cancello chiuso")
#     else:
#
#       if gs == True:
#          print("cancello aperto ")
#          gs = False
#          logging.info("Cancello aperto")
pause()
