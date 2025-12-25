import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
 
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
 
for i in range(5):
   # Gira el motor en un sentido durante 3 segundos
   print("Girando motor en un sentido")
   GPIO.output(6, GPIO.HIGH)
   GPIO.output(13, GPIO.LOW)
   time.sleep(3)
 
  # Gira el motor en el otro sentido durante 3 segundos
   print("Girando motor en sentido contrario")
   GPIO.output(6, GPIO.LOW)
   GPIO.output(13, GPIO.HIGH)
   time.sleep(3)
 
GPIO.cleanup()