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

    os.system("mkdir /home/cam/Desktop/Camera_Tests/" + dt)

    os.system(
    "libcamera-vid --codec libav --camera 0 -t 10000 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast -o /home/cam/Desktop/Camera_Tests/" + dt + "/C0-" + dt + ".mp4" + "&" +
    "libcamera-vid --codec libav --camera 1 -t 10000 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast -o /home/cam/Desktop/Camera_Tests/" + dt + "/C1-" + dt +".mp4")

    red.off()
    blue.blink(on_time=0.2, off_time=0.2,n=5, background=False)
    print("Done!")

    blue.off()


exit()
