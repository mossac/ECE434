#!/usr/bin/python3
# Aidan Moss 9/9/21
import Adafruit_BBIO.GPIO as GPIO
import time
import sys

xsize = input("What width do you want for your game?\n")
ysize = input("What height do you want for your game?\n")
 
arr = [[' ' for i in range(int(xsize))] for j in range(int(ysize))] 

for x in range(int(xsize)):
    for y in range(int(ysize)):
        sys.stdout.write(arr[x][y])
    if y == (int(ysize)-1):  
            sys.stdout.write("\n") 
    
    
xpos =0
ypos =0 
while True:
    
    for x in range(int(xsize)):
        for y in range(int(ysize)):
            sys.stdout.write(arr[x][y])
        if y == (int(ysize)-1):  
                sys.stdout.write("\n") 
    
    print("Cursor pos, Y = " + str(xpos) + " X =" + str(ypos) + " ")
    cmd = input("Next move?\n")
    if cmd == "x": break
    if cmd == "c": arr = [['+' for i in range(int(xsize))] for j in range(int(ysize))] 
    if cmd == "w": xpos-=1
    if cmd == "s": xpos+=1
    if cmd == "a": ypos-=1
    if cmd == "d": ypos+=1
    
    if ypos >= int(ysize): ypos=int(ysize)-1
    if xpos >= int(xsize): xpos=int(xsize)-1
    
    if ypos < 0: ypos=0
    if xpos < 0: xpos=0
    
    arr[xpos][ypos] = 'X'
    