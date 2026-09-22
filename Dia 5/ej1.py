import RPi.GPIO as GPIO
import time

pinv1= 21
pina1= 16
pinr1= 12 
pinv2= 25
pina2= 23
pinr2= 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinv1, GPIO.OUT)
GPIO.setup(pina1, GPIO.OUT)
GPIO.setup(pinr1, GPIO.OUT)
GPIO.setup(pinv2, GPIO.OUT)
GPIO.setup(pina2, GPIO.OUT)
GPIO.setup(pinr2, GPIO.OUT)
try:
    while True:
        GPIO.output(pinv1,True)
        GPIO.output(pinr2,True)

        time.sleep(2)

        GPIO.output(pinv1,False)
        GPIO.output(pina1,True)

        time.sleep(2)

        GPIO.output(pina1,False)
        GPIO.output(pinr1,True)

        time.sleep(2)   

        GPIO.output(pina2,True)

        time.sleep(2)

        GPIO.output(pinr2,False)
        GPIO.output(pina2,False)
        GPIO.output(pinv2,True)

        time.sleep(2)

        GPIO.output(pina2,True)
        GPIO.output(pinv2,False)
        
        time.sleep(2)
        GPIO.output(pina2,False)
        GPIO.output(pinr2,True)
        time.sleep(2)
        GPIO.output(pina1,True)
        time.sleep(2)
        GPIO.output(pina1,False)
        GPIO.output(pinr1,False)
except KeyboardInterrupt:
    print("Saliending")
finally:
    GPIO.cleanup()


