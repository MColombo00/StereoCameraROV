#!/usr/bin/python3
import os, datetime, multiprocessing,time
import gpiozero as GPIO

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
 
#     #Basic timelapse, no image customization
    os.system(
    "rpicam-still --camera 1 --timeout 30000 --timelapse 2000 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast --width 4656 --height 3496 -n -o /home/cam/Desktop/timelapseTest/" + dt + "/C1-%04d.jpg & " +
    "rpicam-still --camera 0 --timeout 30000 --timelapse 2000 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast --width 4656 --height 3496 -n -o /home/cam/Desktop/timelapseTest/" + dt + "/C0-%04d.jpg"
    )
    
    red.off()
    blue.blink(on_time=0.2,off_time=0.2,n=10, background=False)
    print("Done!")

    blue.off()
     
green.off()
exit()
