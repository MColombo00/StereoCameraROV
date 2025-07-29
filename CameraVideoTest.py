#!/usr/bin/python3
import os, datetime, multiprocessing
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
    #print(dt)aa

#     os.system("mkdir /home/cam/Desktop/Camera_Tests/" + dt)
    os.system("mkdir /home/cam/Desktop/timelapseTest/" + dt)

#	Video Test
#     os.system(
#     "rpicam-vid --codec libav --camera 0 -t 10000 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast --width 4656 --height 3496 -o /home/cam/Desktop/Camera_Tests/" + dt + "/C0-" + dt + ".mp4" + "&" +
#     "rpicam-vid --codec libav --camera 1 -t 10000 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast --width 4656 --height 3496 -o /home/cam/Desktop/Camera_Tests/" + dt + "/C1-" + dt +".mp4")

    os.system(
    "rpicam-still --timeout 12000 --timelapse 2000 --camera 0 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast --preview 600,0,700,600 -o /home/cam/Desktop/timelapseTest/" + dt + "/C0-%04d.jpg" + "&" +
    "rpicam-still --timeout 12000 --timelapse 2000 --camera 1 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast --preview 0,0,600,600 -o /home/cam/Desktop/timelapseTest/" + dt + "/C1-%04d.jpg")


#	Hello Test
#     os.system(
#         "libcamera-hello --camera 0 -t 10000 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast --framerate 60 -o /home/cam/Desktop/Camera_Tests/" + dt + "/C0-" + dt + "" + "&" +
#         "libcamera-hello --camera 1 -t 10000 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast --framerate 60 -o /home/cam/Desktop/Camera_Tests/" + dt + "/C1-" + dt +"")

    red.off()
    blue.blink(on_time=0.2, off_time=0.2,n=5, background=False)
    print("Done!")

    blue.off()


exit()
