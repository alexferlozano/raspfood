import RPi.GPIO as GPIO
import time
import requests
import time
import board
import adafruit_dht
from datetime import datetime

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
    

class Sensores:
    def __init__(self, echo, trigger, echo2, trigger2):
        self.echo = echo
        self.trigger = trigger
        self.echo2 = echo2
        self.trigger2 = trigger2
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjMsImlhdCI6MTY2OTk1MzI1OH0.Y4T64-aZz18raBAtD6kGx6pdfH4ptQh_EeWmgDxgLdA'
        #self.dhtDevice = adafruit_dht.DHT11(board.D18)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo2, GPIO.IN)
        GPIO.setup(self.trigger2, GPIO.OUT)
        
    def getUltraData(self):
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
            data = {'value_int':1, 'value_float': abs(distance), 'value_string':'null', 'date':now.isoformat(), 'raspberry_sensor_id': '1'}
            r = requests.post('https://alimdogandcat.space/SensorValues/Create', json=data, auth=BearerAuth(self.token))
            #post = r.json()
            if r.status_code == 200:
                rp = r.json()
                print(rp)
            else:
                print("Error from server: " + str(r.content))
            return
            #time.sleep(3)
        except Exception as e:
            print(e)
        finally:
            print("")
            #GPIO.cleanup()
                
    '''def getTemperatureData(self):
        try:
            temperature_c = self.dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = self.dhtDevice.humidity
            print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                )
            )
            now = datetime.now()
            data = {'value_int':1, 'value_float': temperature_c, 'value_string':'null', 'date':now.isoformat(), 'raspberry_sensor_id': '3'}
            r = requests.post('https://alimdogandcat.space/SensorValues/Create', json=data, auth=BearerAuth(self.token))
            #post = r.json()
            if r.status_code == 200:
                rp = r.json()
                print(rp)
            else:
                print("Error from server: " + str(r.content))
                
            dataTem = {'value_int':1, 'value_float': humidity, 'value_string':'null', 'date':now.isoformat(), 'raspberry_sensor_id': '5'}
            r = requests.post('https://alimdogandcat.space/SensorValues/Create', json=dataTem, auth=BearerAuth(self.token))
            #post = r.json()
            if r.status_code == 200:
                rp = r.json()
                print(rp)
            else:
                print("Error from server: " + str(r.content))

        except RuntimeError as error:
            #self.dhtDevice.exit()
            print(error.args[0])
                #time.sleep(2.0)
                #continue
        except Exception as error: 
            #self.dhtDevice.exit()
            print(error.args[0])
            #raise error'''
            
    def getUltraDataWater(self):
        try:
            GPIO.output(self.trigger2, 1)
            time.sleep(0.00001)
            GPIO.output(self.trigger2, 0)
            
            start_time = time.time()
            end_time = time.time()
            
            while GPIO.input(self.echo2) == 0:
                start_time = time.time()
            
            while GPIO.input(self.echo2) == 1:
                end_time = time.time()
            
            time_elapsed = start_time - end_time
            distance = (time_elapsed * 34300) / 2
            print("Measured distance Ultra Data: %.1f cm" % abs(distance))
            print("--------------------------")
            now = datetime.now()
            data = {'value_int':1, 'value_float': abs(distance), 'value_string':'null', 'date':now.isoformat(), 'raspberry_sensor_id': '2'}
            r = requests.post('https://alimdogandcat.space/SensorValues/Create', json=data, auth=BearerAuth(self.token))
            #post = r.json()
            if r.status_code == 200:
                rp = r.json()
                print(rp)
            else:
                print("Error from server: " + str(r.content))
            return
            #time.sleep(3)
        except Exception as e:
            print(e)
        finally:
            print("")
            #GPIO.cleanup()
