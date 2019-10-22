from machine import DAC, Pin

dac = DAC(Pin(25))
dac.write(128)  