import time
import board
import neopixel
a=-1
c=0
d=0.5
# Configuración del Pixel
pixel_pin = board.D18
num_pixels = 16 # Número de LEDs en tu tira
ORDER = neopixel.GRB # Orden de colores (A veces es RGB)

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


try:
    while True: 
            


            pixels[a]=(0,0,0)
            time.sleep(0.05)
            a=a+1
            pixels[a]=(255,0,0)
            if a==15:
                 a=-1
            
            pixels[c]=(6,7,67)
            d=d+0.5
            if d==a:
                c=c+1
            pixels.show()
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()