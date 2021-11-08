#!/usr/bin/env python
import time

w1="/sys/class/hwmon/hwmon0/temp1_input"
w2="/sys/class/hwmon/hwmon1/temp1_input"

while True:
    raw1 = open(w1, "r").read()
    raw2 = open(w2, "r").read()
    print "Temperature is " + str(float(raw1.split("t=")[-1])/1000) + " degrees from sensor 1"
    print "Temperature is " + str(float(raw2.split("t=")[-1])/1000) + " degrees from sensor 2"
    time.sleep(1)
