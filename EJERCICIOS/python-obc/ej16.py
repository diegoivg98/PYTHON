# Importing the time module.
import time

# Getting the current hour and minutes.
hora = time.strftime('%H') 
minutos = time.strftime('%M')


# Checking if the hour is greater or equal to 19, if it is, it prints "Es hora de irse a casa", if
# not, it prints "Quedan {} horas y {} minutos para irnos a casa".format(19- int(hora),
# 59-int(minutos))
if int(hora) >= 19:
    print ("Es hora de irse a casa") 
else:
    print ("Quedan {} horas y {} minutos para irnos a casa".format(19- int(hora), 59-int(minutos)))