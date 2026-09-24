import time
import board
import neopixel
import random
import RPi.GPIO as GPIO

w=0
boton= 21
vel=0.5
pixel_pin = board.D18
GPIO.setmode(GPIO.BCM)
GPIO.setup(boton,GPIO.IN)
GPIO.setup(boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
num_pixels = 16 
ORDER = neopixel.GRB 

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
def gano():
    for i in range (4):
        pixels.fill((0,255,0))
        pixels.show()
        time.sleep(0.5)
        pixels.fill((0,0,0))
        pixels.show()
        time.sleep(0.5)
    global w
    w=1
    global vel
    vel=vel-0.1
    if vel==0:
        for i in range (4):
            pixels.fill((0,0,0))
            pixels.fill((0,0,255))
            pixels.show()
            time.sleep(0.5)
            pixels.fill((0,0,0))
            pixels.show()
            time.sleep(0.5)
        vel=0.5
        w=1

def perdio():
    for i in range(4):
        pixels.fill((255,0,0))
        pixels.show()
        time.sleep(0.5)
        pixels.fill((0,0,0))
        pixels.show()
        time.sleep(0.5)
        
    global vel
    vel=0.5
    global w
    w=1

try:
    while True:
        w=0
        c=random.randint(0,15)
        while w==0: 
            for i in range(num_pixels):
                pixels[i]=(5,5,5)
                pixels[c]=(255,25,0)
                pixels.show()
                
                if GPIO.input(boton)==False:
                    if (i-1)==c:
                        gano()
                        break
                    else:
                        perdio()
                        break
                time.sleep(vel)
                pixels[i]=(0,0,0)
                pixels.show()

except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()