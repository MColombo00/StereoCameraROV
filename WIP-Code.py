#!/usr/bin/python3
import os, datetime, multiprocessing,time
import gpiozero as GPIO

red = GPIO.LED(14)
blue = GPIO.LED(15)
green = GPIO.LED(18)
sw = GPIO.Button(17)
    
dt = datetime.datetime.now().strftime("%m-%d-%S")

if(os.path.exists("/home/cam/Desktop/Camera_Tests/" + dt)):
    pass
else:
    os.system("mkdir /home/cam/Desktop/Camera_Tests/" + dt)
    
while True:
    green.on()

    sw.wait_for_press()
    green.off()
    blue.blink(on_time=0.5, off_time=0.5, background=True)
    c0 = 0
    c1 = 0
        

    
    #print(dt)

#     os.system("mkdir /home/cam/Desktop/Camera_Tests/" + dt)

# --metadata /home/cam/Desktop/timelapseTest/" + dt + "/C0-%04d.json
# --metadata /home/cam/Desktop/timelapseTest/" + dt + "/C1-%04d.json 


#     #Basic timelapse, no image customization
#     os.system(
#     "rpicam-still --camera 1 --timeout 30000 --timelapse 2000 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast --width 4656 --height 3496 -o /home/cam/Desktop/timelapseTest/" + dt + "/C1-%04d.jpg & " +
#     "rpicam-still --camera 0 --timeout 30000 --timelapse 2000 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast --width 4656 --height 3496 -o /home/cam/Desktop/timelapseTest/" + dt + "/C0-%04d.jpg"
#     )
    
#     #Basic timelapse, no image customization
    os.system(
    f"rpicam-still --camera 1 --timeout 2000 --autofocus-on-capture --autofocus-range full --autofocus-speed fast -o /home/cam/Desktop/Camera_Tests/{dt}/Cam1_{str(c1)}.jpg & " +
    f"rpicam-still --camera 0 --timeout 2000 --autofocus-on-capture --autofocus-range full --autofocus-speed fast -o /home/cam/Desktop/Camera_Tests/{dt}/Cam0_{str(c0)}.jpg"
    )
    c0 += 1
    c1 += 1

    
    print("Done!")

    blue.off()
     
green.off()
exit()

