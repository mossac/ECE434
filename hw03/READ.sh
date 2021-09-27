#!/bin/sh
temp=$(sudo i2cget -y 2 0x49 0)
temp2=$(($temp*3))
echo "Temp is: $temp2"
