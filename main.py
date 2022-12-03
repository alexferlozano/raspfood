'''from testMotor import *
from testTemperature import *
from test import *'''
from sensores import *
import RPi.GPIO as GPIO
import socketio
import asyncio
import aiohttp
import requests
import time

url = "https://alimdogandcat.space"
s = Sensores(23,24,26,19,13,6, True)


while True:
    s.getUltraData()
    s.getTemperatureData()
    time.sleep(5)
#s.moverMotor()

'''sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    
@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})


@sio.on('Motor')
def onMotor():
    print('esta puta mierda ya jaló')
    s.moverMotor()

@sio.event
def disconnect():
    print('disconnected from server')

#sio.connect("ws://alimdogandcat.space/raspberry")
#sio.connect('http://127.0.0.1:3333')
sio.connect('https://alimdogandcat.space')
sio.wait()'''


#GPIO.setmode(GPIO.BCM)
#motor = Motor(26,19,13,6, True)
#sonico = Sonico(23,24)
#motor.girarMotor()
#sonico.getData()
#temperatura = Temperatura()
#temperatura.getData()