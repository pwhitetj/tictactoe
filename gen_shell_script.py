#!/usr/bin/python3

####
# generate a script that runs a bunch of tic tac toe games
####

xstart = 20
ystart = 20
xwidth = 310
ywidth = 350
port = 5010
for xc in range(4):
    for yc in range(3):
        print("python3 ttt.py %i %i random server %i &" % (xstart+xc*xwidth, ystart+yc*ywidth, port))
        print("sleep 0.3")
        port += 1

        
