import RPi.GPIO as GPIO
import time
import requests
from datetime import datetime

'''class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r'''
    
#echo = 23
#trigger = 24

'''GPIO.setmode(GPIO.BCM)

GPIO.setup(echo, GPIO.IN)
GPIO.setup(trigger, GPIO.OUT)'''

class Sonico:
    def __init__(self, echo, trigger):
        self.echo = echo
        self.trigger = trigger
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.setup(self.trigger, GPIO.OUT)
        
    def getData(self):
        try:
            GPIO.output(self.trigger, 1)
            time.sleep(0.00001)
            GPIO.output(self.trigger, 0)
            
            start_time = time.time()
            end_time = time.time()
            
            while GPIO.input(self.echo) == 0:
                start_time = time.time()
            
            while GPIO.input(self.echo) == 1:
                end_time = time.time()
            
            time_elapsed = start_time - end_time
            distance = (time_elapsed * 34300) / 2
            print("Measured distance: %.1f cm" % abs(distance))
            print("--------------------------")
            now = datetime.now()
            '''data = {'value_int':1, 'value_float': abs(distance), 'value_string':'null', 'date':now.isoformat(), 'raspberry_sensor_id': '1'}
            r = requests.post('https://alimdogandcat.space/SensorValues/Create', json=data, auth=BearerAuth('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEsImlhdCI6MTY2NzU4ODQ0MH0.2fTbZWJTcDwvibU9nPefDFq8LSdQjMDXx4OxUbOpCwY'))
            #post = r.json()
            if r.status_code == 200:
                rp = r.json()
                print(rp)
            else:
                print("Error from server: " + str(r.content))'''
            #time.sleep(3)
        except Exception as e:
            print(e)
        finally:
            GPIO.cleanup()
    
    
#killall libgpiod_pulsein