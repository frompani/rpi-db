#!/usr/bin/env python2.7
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
####################################################################
#18-8-17 a banco funziona perfetto da preovare sul campo
####################################################################


####################################################################
#input_pin e GND collegati al contatto normalmente aperto con internal pullup
#contatto aperto --->livello alto; contatto chiuso --->livello basso

contatto1 = 5
contatto2 = 6

####################################################################
GPIO.setup(contatto1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(contatto2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
####################################################################

def my_callback1(channel):
	time.sleep(0.01)
        if GPIO.input(contatto1) != GPIO.LOW: #se ho un livello alto vuol dire che e un disturbo
            return
        # se invece ho livello basso il contatto e stato effettivamente chiuso
        print('Schiacciato pulsante campanello 1')
#        os.system("mpg123 /home/pi/bin/doorbell/mp3/TrainBell.mp3 &")
#	os.system("curl -s http://192.168.10.181:8888/json.htm?type=command&param=udevice&idx=27&nvalue=3")
        GPIO.remove_event_detect(contatto1)
        GPIO.wait_for_edge(contatto1, GPIO.RISING)
        print ('Rilasciato pulsante campanello 1, aspetto 3 s. prima di dare possibilita di risuonare')
        time.sleep(3)
        GPIO.remove_event_detect(contatto1)
        GPIO.add_event_detect(contatto1, GPIO.FALLING, bouncetime=200, callback=my_callback1)

def my_callback2(channel):
	time.sleep(0.01)
        if GPIO.input(contatto2) != GPIO.LOW: #se ho un livello alto vuol dire che e un disturbo
            return
        # se invece ho livello basso il contatto e stato effettivamente chiuso
        print('Schiacciato pulsante campanello 2')
#        os.system('ssh pi@192.168.10.181 "/home/pi/bin/./ora.sh"')
#       os.system("curl -s http://192.168.10.181:8888/json.htm?type=command&param=udevice&idx=27&nvalue=3")
        GPIO.remove_event_detect(contatto2)
        GPIO.wait_for_edge(contatto2, GPIO.RISING)
        print ('Rilasciato pulsante campanello 2, aspetto 3 s. prima di dare possibilita di risuonare')
        time.sleep(3)
        GPIO.remove_event_detect(contatto2)
        GPIO.add_event_detect(contatto2, GPIO.FALLING, bouncetime=200, callback=my_callback2)


####################################################################

GPIO.add_event_detect(contatto1, GPIO.FALLING, bouncetime=200, callback=my_callback1)
GPIO.add_event_detect(contatto2, GPIO.FALLING, bouncetime=200, callback=my_callback2)

####################################################################

while True :
        print ("aspetto")
        time.sleep(60)

