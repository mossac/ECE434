#!/usr/bin/python3
#//////////////////////////////////////
#	blink.py
#	Blinks one LED wired to P9_14.
#	Wiring:	P9_14 connects to the plus lead of an LED.  The negative lead of the
#			LED goes to a 220 Ohm resistor.  The other lead of the resistor goes
#			to ground.
#	Setup:	
#	See:	
#//////////////////////////////////////
import Adafruit_BBIO.GPIO as GPIO
import time

blue = "P9_22"

 
GPIO.setup(blue, GPIO.OUT)
 
while True:
  
    GPIO.output(blue, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(blue, GPIO.LOW)
    time.sleep(0.001)
