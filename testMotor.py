import RPi.GPIO as GPIO
import time


class Motor:
    def __init__(self, in1, in2, in3, in4, direction): 
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.step_sleep = 0.002
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
        GPIO.setmode( GPIO.BCM )
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

    def cleanup(self):
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )
        GPIO.cleanup()
    
# Comienzan los ciclos de giro
    def girarMotor(self):
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
         
        self.cleanup()
        exit( 0 )
        

motor = Motor(26,19,13,6, True)        
motor.girarMotor()
