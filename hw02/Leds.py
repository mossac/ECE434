#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time

white = "P9_12"
red = "P9_16"
green = "P9_14"
blue = "P9_22"

sw1 = "P9_18"
sw2 = "P9_19"
sw3 = "P9_41"
sw4 = "P9_42"
 
GPIO.setup(red, GPIO.OUT)
GPIO.setup(white, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

GPIO.setup(sw4, GPIO.IN)
GPIO.setup(sw3, GPIO.IN)
GPIO.setup(sw2, GPIO.IN)
GPIO.setup(sw1, GPIO.IN)

def whitebut(channel):
    state = GPIO.input(channel)
    GPIO.output(white, state)
def greenbut(channel):
    state = GPIO.input(channel)
    GPIO.output(green, state)
def redbut(channel):
    state = GPIO.input(channel)
    GPIO.output(red, state)
def bluebut(channel):
    state = GPIO.input(channel)
    GPIO.output(blue, state)
    

GPIO.add_event_detect(sw4, GPIO.BOTH, callback=whitebut)
GPIO.add_event_detect(sw3, GPIO.BOTH, callback=greenbut)
GPIO.add_event_detect(sw1, GPIO.BOTH, callback=bluebut)
GPIO.add_event_detect(sw2, GPIO.BOTH, callback=redbut)



    
    
while True:
  
    
    
    
  #  GPIO.output(red, GPIO.HIGH)
  #  GPIO.output(green, GPIO.HIGH)
  #  GPIO.output(blue, GPIO.HIGH)
  #  time.sleep(0.5)
  #  GPIO.output(white, GPIO.LOW)
  #  GPIO.output(red, GPIO.LOW)
  #  GPIO.output(green, GPIO.LOW)
  #  GPIO.output(blue, GPIO.LOW)
    time.sleep(0.5)
    
    
#
#detect wherever:

 