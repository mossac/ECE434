#!/usr/bin/python3
# Aidan Moss 9/9/21
import Adafruit_BBIO.GPIO as GPIO
import time
import sys
import smbus
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2

sw4 = "P9_18"
GPIO.setup(sw4, GPIO.IN)


bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70
myEncoder = RotaryEncoder(eQEP1)
myEncoder.setAbsolute()
myEncoder.enable()
Encoder = RotaryEncoder(eQEP2)
Encoder.setAbsolute()
Encoder.enable()


print('frequency ' + str(myEncoder.frequency))

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

def whitebut(channel):
    print("interrupt!!!!")
    for x in range(int(xsize*2)):
           game[x] = 0x00;

	 
GPIO.add_event_detect(sw4, GPIO.BOTH, callback=whitebut)	 
xsize = 8;
ysize = 8;
 

    
xpos = 0x00
ypos = 0x00 

prev_position = 0
prev1_position = 0

for x in range(int(xsize*2)):
    game[x] = 0x00;

while True:
    
    
   
    
    time.sleep(0.5)
    
    cur_position = myEncoder.position
    cur_position1 = Encoder.position
    print(cur_position1)

    print("Cursor pos, Y = " + str(xpos) + " X =" + str(ypos) + " ")
  
    if (cur_position < prev_position): 
        xpos-=1
        
    if (cur_position > prev_position):  
        xpos+=1
        
       
    if (cur_position1 > prev1_position):  
        ypos+=1
        
    if (cur_position1   < prev1_position):  
        ypos-=1
       
      
        
   
    
   
    if ypos > 7: ypos=7
    if xpos > 7 : xpos=7
    if ypos < 0: ypos=0
    if xpos < 0: xpos=0
    
    if(xpos == 0):
        game[ypos * 2] =  0x01 | game[ypos * 2] 
    
    else:
        game[ypos * 2] =  ( 2<< (xpos-1)) | game[ypos * 2] 
    
    prev_position = cur_position
    prev1_position = cur_position1
    bus.write_i2c_block_data(matrix, 0, game)