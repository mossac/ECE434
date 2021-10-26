#!/usr/bin/env python3
# Aidan Moss 9/9/21
import Adafruit_BBIO.GPIO as GPIO
import time
import blynklib
import os, sys
import smbus

bus = smbus.SMBus(2)  
matrix = 0x70         # Use address 0x70
# Setup the LED
LED = 'P9_14'
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1) 

# Setup the button
button = 'P9_11'
GPIO.setup(button, GPIO.IN)
# print("button: " + str(GPIO.input(button)))

# Get the autherization code (See setup.sh)
BLYNK_AUTH = 'Hyl5s2-_y3cWRvp9USkLHPLsxg5nlNMl'

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)


game= [0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]
clear = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]
	 
	 
xsize = 8;
ysize = 8;
 


ypos = 0x00 
xpos = 0x00

def nextState():
    global xpos, ypos
    if ypos > 7: ypos=7
    if xpos > 7 : xpos=7
    if ypos < 0: ypos=0
    if xpos < 0: xpos=0
    if(xpos == 0):
        game[ypos * 2] =  0x01 | game[ypos * 2] 
    
    else:
        game[ypos * 2] =  ( 2<< (xpos-1)) | game[ypos * 2] 
    
   
   
    bus.write_i2c_block_data(matrix, 0, game)
    time.sleep(.2)

def clear():
    arr = [[' ' for i in range(int(xsize))] for j in range(int(ysize))] 
    for x in range(int(xsize*2)):
        game[x] = 0x00;
    bus.write_i2c_block_data(matrix, 0, game)
            

@blynk.handle_event('write V0')
def my_write_handler(pin, value):
    global xpos
    print('Current V{} xpos: {}'.format(pin, xpos))
    GPIO.output(LED, int(value[0])) 
    if(value): xpos -= 1
    
    nextState()
 
@blynk.handle_event('write V1')
def my_write_handler(pin, value):
    global xpos
    print('Current V{} xpos: {}'.format(pin, xpos))
    if(value ): xpos += 1
    
    nextState()
    
    
@blynk.handle_event('write V3')
def my_write_handler(pin, value):
    global ypos
    print('Current V{} ypos: {}'.format(pin, ypos))
    GPIO.output(LED, int(value[0])) 
    if(value): ypos -= 1
    
    nextState()
 
@blynk.handle_event('write V4')
def my_write_handler(pin, value):
    global ypos
    print('Current V{} ypos: {}'.format(pin, ypos))
    if(value):  ypos += 1
    
    nextState()

@blynk.handle_event('write V5')
def my_write_handler(pin, value):
    global ypos
    print('Clear')
    clear()
       
# This callback is called every time the button changes
# channel is the name of the pin that changed
def pushed(channel):
    # Read the current value of the input
    state = GPIO.input(channel)
    print('Edge detected on channel {}, value={}'.format(channel, state))
    # Write it out
    GPIO.output(LED, state)     # Physical LED
    blynk.virtual_write(10, 255*state)  # Virtual LED: 255 max brightness

# This is a non-blocking event 
GPIO.add_event_detect(button, GPIO.BOTH, callback=pushed) 


while True:
    blynk.run()
   
    

    
    
