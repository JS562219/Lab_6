from machine import Pin, ADC, PWM
import time

pwm28 = PWM(Pin(28), freq = 100000) # Initialize Pin 28 using PWM

while True:     # creates a loop
    
    pwm28.duty_u16(65535) 

    pwm28.duty_u16(0)

