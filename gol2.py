#Game of Life - attempt 2 (hopefully faster)
#2-D, 2-state CA with r=1 (all eight squares surrounding a square): 0 = dead cell, 1 = living cell

#This particular program is meant to find the best utilization of Python to create the array and apply the transition rules

#Transition Rules
#1. A living cell (1) with less than two living neighbors dies (loneliness)
#2. A living cell with more than three living neighbors dies (over-crowding)
#3. A living cell with 2 or 3 living neighbors lives (ideal iving conditions)
#4. A dead cell with haveing exactly three living neighbors becomes alive (offspring)

import random
import numpy as np
import matplotlib.pyplot as plt
import array
#from pylab import *
from matplotlib import animation
#import os
plt.rcParams['animation.ffmpeg_path'] = '/Applications/ffmpeg'


CA_size = 64
generations = 1024
g_t = 0

fps = 30

#seeded starts

cel = np.zeros((CA_size,CA_size))
r_pentomino = [[0,1,1],[1,1,0],[0,1,0]]
cel[14:17,14:17] = r_pentomino
ttag = 'r_pentomino'

#random start with x_on% on

#cel_off = 0.85
#cel_rand = np.random.rand(CA_size, CA_size)
#cel = np.piecewise(cel_rand, [cel_rand < cel_off, cel_rand >= cel_off], [0, 1])
#ttag = 'random'


print g_t, cel.sum(), ';',               

fig = plt.figure("Conway's Game of Life")
ax = fig.add_subplot(111)

im = []                                             
im.append([plt.imshow(cel, cmap=plt.cm.gist_yarg, interpolation='nearest')])
                                                                                                                                                                                                                                                                              
for t in range(generations):
    rows = cel+np.roll(cel,1,0)+np.roll(cel,-1,0)
    cols = rows+np.roll(rows,1,1)+np.roll(rows,-1,1)
    
    a_cel = np.piecewise(cols, [cols < 3, cols == 3, cols == 4, cols > 4],[0,3,5,0])
    b_cel = cel + a_cel
    new_cel = np.piecewise(b_cel, [b_cel < 3, b_cel == 3, b_cel == 4, b_cel == 5, b_cel == 6, b_cel > 6],[0,1,1,0,1,0])

    g_t += 1
    print g_t, new_cel.sum(), ';', 
    cel = new_cel

    frame = ax.imshow(cel, cmap=plt.cm.gist_yarg, interpolation='nearest')
    t = ax.annotate(g_t,(1,1))
   
    im.append([frame,t])

im_ani = animation.ArtistAnimation(fig, im, interval = 100, repeat_delay = 1000)
#im_ani.save('gol-'+ttag+'.mp4', writer=animation.FFMpegWriter(), fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
