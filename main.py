import psutil
from playsound import playsound

if psutil.sensors_battery().power_plugged == True:
    if int(psutil.sensors_battery().percent)==100:
        playsound('https://github.com/Angana007/battery-safe-or-unsafe/blob/main/drums.wav')
    else:
        exit()

        
        
if psutil.sensors_battery().power_plugged == False:
    if int(psutil.sensors_battery().percent)==20:
        playsound('https://github.com/Angana007/battery-safe-or-unsafe/blob/main/drums.wav')
    else:
        exit()
