HW07

Files:
hello3.pru0.c
pwm1.pru0.c
Makefile
LED.gpio.png
PWN.png



DESC:
hello3.pru0.c: Blinks LED on P9_31 using gpio front end and has PRU used to trigger the gpio port

pwm1.pru0.c: Uses PRU registers to generate PWN on P9_31 at around 50 MHz.

Makefile: Makefile to help run 

LED.gpio: Screenshot of oscilloscope readout from running hello3.pru0

PWM.png: Screenshot of  oscilloscope readout from running PWM.pru0

How to Use:

hello3.pru0.c: run command $config-pin P9_31 gpio to set P9_31 as correct type, then run
            $make TARGET=hello3.pru0 to load code to PRU, this may fail the first time 
            as the system says it does not have access to /sys if this happens just run it again
            and this fixes the issue

pwm1.pru0.c: Same as the previous file expect you should run $config-pin P9_31 pruout
            into $make TARGET=pwm1.pru0

Question answers:

Q: How fast can you toggle the pin? Is there jitter1? Is it stable?
A: Runs at 1.66 Mhz and there is a decent amout of jitter/ noise with this signal.

Q: What’s the Std Dev? Is there jitter. Comment on how Stable the waveform is
A: Std Dev is around 200 Khz, it is very stable but looks more like a sin wave than
    a PWN signal
