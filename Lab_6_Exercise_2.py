from machine import Pin, ADC, PWM
import time

pwm28 = PWM(Pin(0), freq = 1000000) # Initialize Pin 28 using PWM

while True:

    pwm28.duty_u16(65535) 


# Tested Duty Cycles
# pwm28.duty_u16(1) 
# pwm28.duty_u16(8200) 
# pwm28.duty_u16(16400) 
# pwm28.duty_u16(51000) 
# pwm28.duty_u16(65534) 
# pwm28.duty_u16(65536) 

