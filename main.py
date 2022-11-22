'''from testMotor import *
from testTemperature import *
from test import *'''
from sensores import *
import RPi.GPIO as GPIO


s = Sensores(23,24,26,19,13,6, True)
s.getUltraData()
s.getTemperatureData()
s.moverMotor()

#GPIO.setmode(GPIO.BCM)
#motor = Motor(26,19,13,6, True)
#sonico = Sonico(23,24)
#motor.girarMotor()
#sonico.getData()
#temperatura = Temperatura()
#temperatura.getData()