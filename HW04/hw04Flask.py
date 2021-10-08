#!/usr/bin/python3
# Aidan Moss 9/9/21
import Adafruit_BBIO.GPIO as GPIO
import time
import sys
import smbus
from flask import Flask, render_template, request
app = Flask(__name__)
ledRed = "P9_14"
GPIO.setup(ledRed, GPIO.OUT)   
# turn leds OFF 
GPIO.output(ledRed, GPIO.HIGH)
bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

smile = [0x00, 0x3c, 0x00, 0x42, 0x28, 0x89, 0x04, 0x85,
    0x04, 0x85, 0x28, 0x89, 0x00, 0x42, 0x00, 0x3c
]
frown = [0x3c, 0x00, 0x42, 0x00, 0x85, 0x20, 0x89, 0x00,
    0x89, 0x00, 0x85, 0x20, 0x42, 0x00, 0x3c, 0x00
]
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

def clear():
    arr = [[' ' for i in range(int(xsize))] for j in range(int(ysize))] 
    for x in range(int(xsize*2)):
        game[x] = 0x00;
   
            
@app.route("/")
def index():
	# Read Sensors Status
	xpos = 0x00
	templateData = {
              'title' : 'GPIO output Status!',
              'xpos'  : xpos,
              'ypos' :  ypos
        }
	return render_template('index6.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName,action):
	if deviceName == 'MOVE':
	    global xpos, ypos
	

	if action == "Up":
	    xpos+=1
	
		
	if action == "Down":
	    xpos-=1
		
	if action == "Left":
	    ypos-=1
	
	if action == "Right":
	    ypos+=1
	
	if action == "Clear":
	    clear()
	    
	templateData = {
              'xpos'  : xpos,
              'ypos' :  ypos
	}
    
    
	nextState()
    
	return render_template('index6.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)
    
    

      
        
   
    
   

    