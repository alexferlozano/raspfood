import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(13, GPIO.OUT)
 
for i in range(1):
   # Gira el motor en un sentido durante 3 segundos
   print("Girando motor en un sentido")
   GPIO.output(13, GPIO.LOW)
   time.sleep(.500)
 
  # Gira el motor en el otro sentido durante 3 segundos
   print("Girando motor en sentido contrario")
   GPIO.output(13, GPIO.HIGH)
   time.sleep(.500)
 
GPIO.cleanup()