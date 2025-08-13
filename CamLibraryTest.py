#!/usr/bin/python3
import os, datetime,time
import gpiozero as GPIO
from picamera2 import Picamera2

red = GPIO.LED(14)
blue = GPIO.LED(15)
green = GPIO.LED(18)
sw = GPIO.Button(17)

    
while True:
    green.on()
    
    sw.wait_for_press()
    green.off()
    red.blink(on_time=0.5, off_time=0.5, background=True)
        
    dt = datetime.datetime.now().strftime("%m-%d-%y_%I%M%S")
    os.system("mkdir /home/cam/Desktop/timelapseTest/" + dt)
 


    picam2a = Picamera2(0)
    picam2b = Picamera2(1)
    picam2a.start()
    picam2b.start()
    
    
    
    red.off()
    blue.blink(on_time=0.2,off_time=0.2,n=10, background=False)
    print("Done!")
    blue.off()
     
green.off()
exit()

