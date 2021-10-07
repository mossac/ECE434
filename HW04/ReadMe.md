Homework 4: Aidan Moss

Files:
Leds.py
fastToggle.py
text.sh
hw04Flask.py
LCDText amd BorisLCD


Descriptions:
Leds.py: using mmap to toggle gpio ports using two buttons that control LEDS, USR1 
        and USR3

fastToggle.py: All the functionality of LEDs.py but also has a toggle in the main 
        while loop. This quickly turns a external LED on and off. I measured this 
        on an oscilloscope and this was was much faster than previous measurements
        and it got even faster when i removed the sleep.


text.sh: use bash text.sh to display a pretty picture featuring a banana with text
        overlayed on it that reads "I Love Linux-AidanMoss" on a external LCD
        
hw04Flask.py: creates a webpage using flask, there on 4 buttons on the website,
            that are named down,up,left,right respectively. using these buttons 
            you canv control etech a sketch on the LEDMatix
        
LCDText amd BorisLCD: Pictures of the LCD with text overlayed on a picture and a
        picture of Boris on my LCD
