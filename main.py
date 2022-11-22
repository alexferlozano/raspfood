from testMotor import *
from testTemperature import *
from test import *
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#motor = Motor(26,19,13,6, True)
sonico = Sonico(23,24)
#motor.girarMotor()
sonico.getData()
#temperatura = Temperatura()
#temperatura.getData()