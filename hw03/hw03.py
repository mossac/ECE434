#!/usr/bin/python3
# Aidan Moss 9/9/21
import Adafruit_BBIO.GPIO as GPIO
import time
import sys
import smbus

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
 

    
xpos = 0x00
ypos = 0x00 



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