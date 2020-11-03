from gpiozero  import  Buzzer
from time import sleep

bz = Buzzer(3)
x=1
while x<20:

        for a in range (0, 1000):
                bz.on()
                sleep(0.00051)
                bz.off()
                sleep(0.00051)
        sleep(1)
        x=x+1
