import RPi.GPIO as GPIO
import time

pin = 13

echo = 13
trigger = 18 

GPIO.setmode(GPIO.BCM)

GPIO.setup(trigger, GPIO.OUT)

try:
    while True:
        GPIO.output(trigger, 1)
        time.sleep(0.00001)
        GPIO.output(trigger, 0)
        
        start_time = time.time()
        end_time = time.time()
        
        while GPIO.input(echo) == 0:
            start_time = time.time()
        
        while GPIO.input(echo) == 1:
            end_time = time.time()
        
        time.sleep(3)
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
