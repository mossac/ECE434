#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
from mmap import mmap
import time, struct

white = "P9_12"
red = "P9_16"



sw3 = "P9_41"
sw4 = "P9_42"

GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
USR1= 1<<22
USR3 = 1<<24
P9_14 = 1<<18


with open("/dev/mem", "r+b" ) as f:
  mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)

packed_reg = mem[GPIO_OE:GPIO_OE+4]
reg_status = struct.unpack("<L", packed_reg)[0]
reg_status &= ~(USR1)
reg_status &= ~(USR3 )
mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)


GPIO.setup(sw4, GPIO.IN)
GPIO.setup(sw3, GPIO.IN)


def whitebut(channel):
    state = GPIO.input(channel)
    if(state == 1):
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", USR3 )
    else:
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", USR3 )
def greenbut(channel):
    state = GPIO.input(channel)
    if(state == 1):
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", USR1)
    else:
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", USR1)


GPIO.add_event_detect(sw4, GPIO.BOTH, callback=whitebut)
GPIO.add_event_detect(sw3, GPIO.BOTH, callback=greenbut)




    
    
while True:
    
    if(mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] == struct.pack("<L", P9_14)):
        printf("Button Press")
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", USR1)
    
    time.sleep(0.5)
    
    

    
    
    

 