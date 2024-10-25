from machine import Pin, ADC, PWM
import time

p28 = Pin(0,Pin.OUT)

while True:     # creates a loop
    
    p28.on()
    p28.off()

