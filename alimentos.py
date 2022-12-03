from sensores import *
import RPi.GPIO as GPIO
import socketio
import asyncio
import aiohttp
import requests
import time

url = "https://alimdogandcat.space"
s = Sensores(23,24,16,20)

while True:
    s.getUltraDataWater()
    #s.getUltraData()
    #s.getTemperatureData()
    time.sleep(60)


#GPIO.setmode(GPIO.BCM)
#motor = Motor(26,19,13,6, True)
#sonico = Sonico(23,24)
#motor.girarMotor()
#sonico.getData()
#temperatura = Temperatura()
#temperatura.getData()