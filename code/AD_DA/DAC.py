import spidev
import RPi.GPIO as GPIO
import time

SPI = spidev.SpiDev(0, 0)
pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
SPI.max_speed_hz = 20000
SPI.mode = 0b01


while(1):
    GPIO.output(pin,1)
    time.sleep(0.1)
    GPIO.output(pin,0)
    time.sleep(0.1)
    print("ok")
