#from sensores import *
from testMotor import *
import RPi.GPIO as GPIO
import socketio
import asyncio
import aiohttp
import requests
import time

GPIO.setmode(GPIO.BCM)

#motor = Motor(26,19,13,6, True)
#led = Leds(24,13,19)
#s = Sensores(23,24,26,19,13,6, True)
sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    
@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})


@sio.on('Motor')
def onMotor():
    print('esta puta mierda ya funciona')
    #s.moverMotor()
    print("Girando motor en un sentido")
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)
    time.sleep(1)
    print("Girando motor en sentido contrario")
    GPIO.output(6, GPIO.HIGH)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    #motor.girarMotor()

@sio.on('Pump')
def onPump():
    print('ya jalo la puta bomba')
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, GPIO.LOW)
    time.sleep(1)
 
    print("Girando motor en sentido contrario")
    GPIO.output(19, GPIO.HIGH)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('https://alimdogandcat.space')
sio.wait()