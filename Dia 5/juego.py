import time
import board
import neopixel
import random
import RPi.GPIO as GPIO
a=-1
c=random.randint(0,15)
boton= 21
vel=1
# Configuración del Pixel
pixel_pin = board.D18
GPIO.setmode(GPIO.BCM)
GPIO.setup(boton,GPIO.IN)

num_pixels = 16 # Número de LEDs en tu tira
ORDER = neopixel.GRB # Orden de colores (A veces es RGB)

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)



try:
    while True: 
            pixels[a]=(0,0,0)
            time.sleep(vel)
            a=a+1
            pixels[a]=(255,0,0)
            if a==15:
                 a=-1
            
            pixels[c]=(6,7,67)
            
            if boton==True and a==c:
                vel=vel-0.2
                c=random.randint(0,15)    
            
            if vel==0:
                for i in range(5):
                    pixels[0,1,2,3,4,5]=(4,4,4)
                    pixels.show()
                    time.sleep(0,5)
                    pixels[0,1,2,3,4,5]=(0,0,0)
                    pixels.show()

            pixels.show()
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()