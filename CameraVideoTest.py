import os, datetime, multiprocessing

dt = datetime.datetime.now().strftime("%m-%d-%y_%I%M%S")
#print(dt)

os.system("mkdir /home/cam/Desktop/Camera_Tests/" + dt)


os.system("libcamera-still --camera 1 -t 10000 --autofocus-mode continuous --autofocus-range full --autofocus-speed fast -o /home/cam/Desktop/Camera_Tests/" + dt + "/C1-" + dt + "&"
)

print("Done!")

exit()