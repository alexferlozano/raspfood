import RPi.GPIO as GPIO
import time
import requests
import time
import board
import adafruit_dht
from datetime import datetime


class Sensores:
    def __init__(self, echo, trigger, in1, in2, in3, in4, direction):
        self.echo = echo
        self.trigger = trigger
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.step_sleep = 0.002
        self.dhtDevice = adafruit_dht.DHT11(board.D18)
        self.step_count = 4096 # 5.625*(1/64) por paso, 4096 pasos corresponden a 360°
        self.direction = direction # True para el sentido del reloj, False para el sentido contrario
        self.step_sequence = [[1,0,0,1],
                             [1,0,0,0],
                             [1,1,0,0],
                             [0,1,0,0],
                             [0,1,1,0],
                             [0,0,1,0],
                             [0,0,1,1],
                             [0,0,0,1]]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup( self.in1, GPIO.OUT )
        GPIO.setup( self.in2, GPIO.OUT )
        GPIO.setup( self.in3, GPIO.OUT )
        GPIO.setup( self.in4, GPIO.OUT )
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )
        self.motor_pins = [self.in1,self.in2,self.in3,self.in4]
        self.motor_step_counter = 0 ;
        
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
            print("")
            #GPIO.cleanup()
                
    def getTemperatureData():
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
            '''data = {'value_int':1, 'value_float': temperature_c, 'value_string':'null', 'date':now.isoformat(), 'raspberry_sensor_id': '2'}
            r = requests.post('https://alimdogandcat.space/SensorValues/Create', json=data, auth=BearerAuth('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEsImlhdCI6MTY2NzU4ODQ0MH0.2fTbZWJTcDwvibU9nPefDFq8LSdQjMDXx4OxUbOpCwY'))
            #post = r.json()
            if r.status_code == 200:
                rp = r.json()
                print(rp)
            else:
                print("Error from server: " + str(r.content))'''

        except RuntimeError as error:
            #self.dhtDevice.exit()
            print(error.args[0])
                #time.sleep(2.0)
                #continue
        except Exception as error: 
            #self.dhtDevice.exit()
            raise error
        
    def cleanup(self):
        self.dhtDevice.exit()
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )
        GPIO.cleanup()
    
    def moverMotor(self):
        try:
            i = 0
            for i in range(self.step_count):
                for pin in range(0, len(self.motor_pins)):
                    GPIO.output( self.motor_pins[pin], self.step_sequence[self.motor_step_counter][pin] )
                if self.direction==True:
                    self.motor_step_counter = (self.motor_step_counter - 1) % 8
                elif self.direction==False:
                    self.motor_step_counter = (self.motor_step_counter + 1) % 8
                else: # Programación defensiva
                    print( "No debería llegar a este punto por que la dirección siempre es verdadera o falsa" )
                    self.cleanup()
                    exit( 1 )
                time.sleep( self.step_sleep )
            
        except KeyboardInterrupt:
            self.cleanup()
            exit( 1 )
            
        #self.cleanup()
        exit( 0 )
            
        
