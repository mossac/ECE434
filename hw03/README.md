HW03

Files:
Read.py
READ.sh
hw03.pyhw03.Encoder.py
hw03
setup.sh

DESC:
hw03:
    Very similar to previous etch a sketch program from homework 1, uses keyboard commands 
    to control etch a sketch on 8x8 LED matrix
        w- go up
        s- go up
        a- go left
        d-go right
        c- clear screen
        x- kill program safely

READ.sh
    Reads in values from TMP101 sensor and converts to F using shell commands from 
    data on pin 19 and 20
    
Read.py 
    Reads in value from TMP101 sensor and converts to F but using python instead of s
    hell commands. Uses same pins as READ.sh
    

hw03.Encoder
    etcha sketch program but uses input from two encoders as controls to move player in game
    also features a clear button connected to gpio on pin 18. Must run setup.sh file before 
    trying to run this file in order to assign correct ports to eqep. 
        Encoder on eqep2 = clockwise -> right
                           counterclockwise -> left
        Encoder on eqep1 = clockwise -> down
                           counterclockwise -> up
        switch on p9_18 = clear
    
setup.sh
    assigns pins to use eqep
    
   
# hw03 grading

| Points      | Description |
| ----------- | ----------- |
|  5/5 | TMP101 
|  3/3 |   | setup.sh
|  2/2 |   | Documentation 
|  5/5 | Etch-a-Sketch
|  3/3 |   | setup.sh
|  2/2 |   | Documentation
| 20/20 | **Total**

Looks Good.