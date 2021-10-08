Homework 4: Aidan Moss

Files:
Leds.py
fastToggle.py
text.sh
hw04Flask.py
LCDText amd BorisLCD
ReadTemp.sh


Descriptions:
Leds.py: using mmap to toggle gpio ports using two buttons that control LEDS, USR1 
        and USR3

fastToggle.py: All the functionality of LEDs.py but also has a toggle in the main 
        while loop. This quickly turns a external LED on and off. I measured this 
        on an oscilloscope and this was was much faster than previous measurements
        and it got even faster when i removed the sleep.

*How fast was it?*

text.sh: use bash text.sh to display a pretty picture featuring a banana with text
        overlayed on it that reads "I Love Linux-AidanMoss" on a external LCD
        
hw04Flask.py: creates a webpage using flask, there on 4 buttons on the website,
            that are named down,up,left,right respectively. using these buttons 
            you canv control etech a sketch on the LEDMatix
        
LCDText amd BorisLCD: Pictures of the LCD with text overlayed on a picture and a
        picture of Boris on my LCD
<<<<<<< HEAD
        
ReadTemp.sh: Reads the data in from the TMP101 tempurature sensor using the kernel driver. T
        hen output this to the terminal/
=======

# hw04 grading

| Points      | Description |
| ----------- | ----------- |
|  0/2 | Memory map     | *Missing*
|  4/4 | mmap()
|  0/4 | i2c via Kernel | *Missing*
|  0/5 | Etch-a-Sketch via flask | *Need to demo*
|  0/5 | LCD display    | *Need to demo*
|      | Extras
| 4/20 | **Total**

*My comments are in italics. --may*

>>>>>>> 66e0e55a34b00083c65e067c61dbfa6d20c866b7
