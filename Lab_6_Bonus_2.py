from machine import Pin, ADC, PWM
from time import sleep

p27 = ADC(Pin(27)) # Set ADC read to Pin 27
pwm28 = PWM(Pin(28), freq = 1000000) # Initialize Pin 28 using PWM

while True:     # creates a loop
    print(p27.read_u16())   # Output the value from the potentiometer to Terminal from Pin 27
    pwm28.duty_u16(p27.read_u16()) # Set Pin 28 to the value from Pin 27 and the potentiometer
    sleep(0.1) # Sets the time between each update to pin 28 and printout


