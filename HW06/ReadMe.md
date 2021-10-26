HW06 Aidan Moss

Files:
RTTEST.png
NORTEST.png
vidNotes.txt


Descriptions:
VidNotes: My answers to the questions from the video "What Every Driver Developer Should Now"

*It's empty*

RTTEST.png: Results from cyclic test on Real time kernel both udner load and 
    not under load
    
NORTTEST: Same as RTTEST.png but for the non-real time kernel.


Comments on Plots:
    Q: What are you using for a load?:
    A: I compiled a simple c file, cleaned up the result and then compiled again
    until the test was done.
    
    Q:Does the RT kernel have a bounded latency
    A:The lastency appears to be bounded to 200ms as we notice a sharp drop off
    as the plot approaches that mark
    
# hw06 grading

| Points      | Description |
| ----------- | ----------- |
|  2/2 | Project 
|  0/5 | Questions | *empty*
|  4/4 | PREEMPT_RT
|  2/2 | Plots to 500 us
|  5/5 | Plots - Heavy/Light load
|  2/2 | Extras
| 15/20 | **Total**

*My comments are in italics. --may*

