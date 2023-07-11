import RPi.GPIO as GPIO
import time

class Main_IO:
    def __init__(self,pin_in,pin_out):
        GPIO.setmode(GPIO.Board)  # Board pin-numbering scheme
        self.input_pin = pin_in
        self.output_pin= pin_out
        self.curr_value=GPIO.input(self.input_pin)
        # set pins as input and output
        GPIO.setup(self.input_pin, GPIO.IN) 
        GPIO.setup(self.output_pin, GPIO.OUT, initial=GPIO.LOW) 
    def send(self):
        GPIO.output(self.output_pin, GPIO.HIGH) 
    def send_close(self):
        GPIO.output(self.output_pin, GPIO.LOW)  
    


IO=Main_IO()#define input an output
IO.send()
#jetson send signal to let robot pick the first bottle

prev_value=None

while True:
    try:
         if IO.curr_value != prev_value:
            if IO.curr_value==GPIO.HIGH: 
                IO.send_close()
                #trigger photo taking    
            prev_value=IO.curr_value          
    except: print("IO connection issue")
        
        
    #elif examine picture taken and saved
    #IO.send()
