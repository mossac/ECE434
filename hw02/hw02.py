#!/usr/bin/python3
# Aidan Moss 9/9/21
import Adafruit_BBIO.GPIO as GPIO
import time
import sys


sw1 = "P9_18"
sw2 = "P9_19"
sw3 = "P9_41"
sw4 = "P9_42"
xpos = 0
ypos = 0 

GPIO.setup(sw4, GPIO.IN)
GPIO.setup(sw3, GPIO.IN)
GPIO.setup(sw2, GPIO.IN)
GPIO.setup(sw1, GPIO.IN)

xsize = input("What width do you want for your game?\n")
ysize = input("What height do you want for your game?\n")
 
arr = [[' ' for i in range(int(xsize))] for j in range(int(ysize))] 

for x in range(int(xsize)):
    for y in range(int(ysize)):
        sys.stdout.write(arr[x][y])
    if y == (int(ysize)-1):  
            sys.stdout.write("\n") 
    
    


def whitebut(channel):
    global xpos
    global ypos
    for x in range(int(xsize)):
        for y in range(int(ysize)):
            sys.stdout.write(arr[x][y])
        if y == (int(ysize)-1):  
                sys.stdout.write("\n") 
    
    print("Cursor pos, Y = " + str(xpos) + " X =" + str(ypos) + " ")
    
   
    xpos-=1
 
    if ypos >= int(ysize): ypos=int(ysize)-1
    if xpos >= int(xsize): xpos=int(xsize)-1
    
    if ypos < 0: ypos=0
    if xpos < 0: xpos=0
    
    arr[xpos][ypos] = 'X'
    
def greenbut(channel):
    global xpos
    global ypos
    for x in range(int(xsize)):
        for y in range(int(ysize)):
            sys.stdout.write(arr[x][y])
        if y == (int(ysize)-1):  
                sys.stdout.write("\n") 
    
    print("Cursor pos, Y = " + str(xpos) + " X =" + str(ypos) + " ")
        
   
    xpos+=1
 
    if ypos >= int(ysize): ypos=int(ysize)-1
    if xpos >= int(xsize): xpos=int(xsize)-1
    
    if ypos < 0: ypos=0
    if xpos < 0: xpos=0
    
    arr[xpos][ypos] = 'X'
    
def redbut(channel):
    global xpos
    global ypos
    for x in range(int(xsize)):
        for y in range(int(ysize)):
            sys.stdout.write(arr[x][y])
        if y == (int(ysize)-1):  
                sys.stdout.write("\n") 
    
    print("Cursor pos, Y = " + str(xpos) + " X =" + str(ypos) + " ")
    
   
    ypos-=1
 
    if ypos >= int(ysize): ypos=int(ysize)-1
    if xpos >= int(xsize): xpos=int(xsize)-1
    
    if ypos < 0: ypos=0
    if xpos < 0: xpos=0
    
    arr[xpos][ypos] = 'X'
    
def bluebut(channel):
    global xpos
    global ypos
    for x in range(int(xsize)):
        for y in range(int(ysize)):
            sys.stdout.write(arr[x][y])
        if y == (int(ysize)-1):  
                sys.stdout.write("\n") 
    
    print("Cursor pos, Y = " + str(xpos) + " X =" + str(ypos) + " ")
    
   
    ypos+=1
 
    if ypos >= int(ysize): ypos=int(ysize)-1
    if xpos >= int(xsize): xpos=int(xsize)-1
    
    if ypos < 0: ypos=0
    if xpos < 0: xpos=0
    
    arr[xpos][ypos] = 'X'
    

GPIO.add_event_detect(sw4, GPIO.RISING, callback=whitebut, bouncetime=100)
GPIO.add_event_detect(sw3, GPIO.RISING, callback=greenbut, bouncetime=100)
GPIO.add_event_detect(sw1, GPIO.RISING, callback=bluebut, bouncetime=100)
GPIO.add_event_detect(sw2, GPIO.RISING, callback=redbut, bouncetime=100)


while True:
    cmd = input("Next move?\n")
    if cmd == "x": break
    if cmd == "c": 
        arr = [[' ' for i in range(int(xsize))] for j in range(int(ysize))] 
        for x in range(int(xsize)):
            for y in range(int(ysize)):
                sys.stdout.write(arr[x][y])
            if y == (int(ysize)-1):  
                sys.stdout.write("\n") 
    time.sleep(0.5)
    
    