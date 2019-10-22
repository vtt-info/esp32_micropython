import time
from machine import Pin, PWM

led_1 = PWM(Pin(25)) # Setter opp PWM på Pinne med standard verdier
led_1.freq() # Returnerer frekvensen på pwm 
led_1.duty()
led_1.freq(4000) # Setter frekvensen til 4000Hz
led_1.duty(512) # Setter duty til 512 av 1024 - 50%

for i in range(512): # Øker styrken fra 0 til 50%
    led_1.duty(i) 
    time.sleep(0.2) # Øker intensitetetn sakte 

