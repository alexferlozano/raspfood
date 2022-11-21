import RPi.GPIO as GPIO
import time
 
in1 = 26
in2 = 19
in3 = 13
in4 = 6
 
step_sleep = 0.002
 
step_count = 4096 # 5.625*(1/64) por paso, 4096 pasos corresponden a 360°
direction = True # True para el sentido del reloj, False para el sentido contrario
 
# Se define la secuencia de fases para el motor
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]
# Se establecen los pines de salida de la Raspberry
GPIO.setmode( GPIO.BCM )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )
# Se inicializan los estados de los pines
GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )
motor_pins = [in1,in2,in3,in4]
motor_step_counter = 0 ;

def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup()
    
# Comienzan los ciclos de giro
try:
    i = 0
    for i in range(step_count):
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
        if direction==True:
            motor_step_counter = (motor_step_counter - 1) % 8
        elif direction==False:
            motor_step_counter = (motor_step_counter + 1) % 8
        else: # Programación defensiva
            print( "No debería llegar a este punto por que la dirección siempre es verdadera o falsa" )
            cleanup()
            exit( 1 )
        time.sleep( step_sleep )
 
except KeyboardInterrupt:
    cleanup()
    exit( 1 )
 
cleanup()
exit( 0 )