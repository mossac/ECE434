#!/usr/bin/env python3
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
'''
	Raspberry Pi GPIO Status and Control
'''
import Adafruit_BBIO.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
#define LED GPIOs
ledRed = "P9_15"
#initialize GPIO status variable
ledRedSts = 0
# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)   
# turn leds OFF 
GPIO.output(ledRed, GPIO.HIGH)

@app.route("/")
def index():
	# Read Sensors Status
	ledRedSts = GPIO.input(ledRed)
	templateData = {
              'title' : 'GPIO output Status!',
              'ledRed'  : ledRedSts,
        }
	return render_template('index3.html', **templateData)
	
@app.route("/<deviceName>/action")
def action(deviceName, action):
	if deviceName == 'ledRed':
		actuator = ledRed

	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		     
	ledRedSts = GPIO.input(ledRed)
	
	templateData = {
              'ledRed'  : ledRedSts,
	}
	return render_template('index3.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)
   
   
while True:
    
    
    
    print("Cursor pos, Y = " + str(xpos) + " X =" + str(ypos) + " ")
    cmd = input("Next move?\n")
    if cmd == "x": break
    if cmd == "c": 
        arr = [[' ' for i in range(int(xsize))] for j in range(int(ysize))] 
        for x in range(int(xsize*2)):
            game[x] = 0x00;
    if cmd == "w": 
        xpos-=1
        
        
    if cmd == "s": 
        xpos+=1
        
       
    if cmd == "a": 
        ypos+=1
        
        
    if cmd == "d": 
        ypos-=1
       
      
        
   
    
   
    if ypos > 7: ypos=7
    if xpos > 7 : xpos=7
    if ypos < 0: ypos=0
    if xpos < 0: xpos=0
    if(xpos == 0):
        game[ypos * 2] =  0x01 | game[ypos * 2] 
    
    else:
        game[ypos * 2] =  ( 2<< (xpos-1)) | game[ypos * 2] 
    
   
   
    bus.write_i2c_block_data(matrix, 0, game)