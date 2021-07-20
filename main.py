import psutil
from playsound import playsound

if psutil.sensors_battery().power_plugged == True:
    if int(psutil.sensors_battery().percent)==100:
        playsound('/home/angana/Downloads/drums.wav')
    else:
        exit()
