# Here's how to use imagemagick to display text
# Make a blank image
convert banana.jpg -gravity Center  -pointsize 70 -annotate 0 'I Love Linux-AidanMoss' temp1.jpg



sudo fbi -noverbose -T 1 -a temp1.jpg
