#Game of Life - attempt 2 (hopefully faster)
#2-D, 2-state CA with r=1 (all eight squares surrounding a square): 0 = dead cell, 1 = living cell

#Transition Rules
#1. A living cell (1) with less than two living neighbors dies (loneliness)
#2. A living cell with more than three living neighbors dies (over-crowding)
#3. A living cell with 2 or 3 living neighbors lives (ideal iving conditions)
#4. A dead cell with haveing exactly three living neighbors becomes alive (offspring)

import random
import numpy as np
import matplotlib.pyplot as plt
import array
from pylab import *
from matplotlib import animation
import os
plt.rcParams['animation.ffmpeg_path'] = '/Applications/ffmpeg'


CA_size = 32
generations = 128
g_t = 0

#random start with x_on% on
cel_off = 0.85
cel_rand = np.random.rand(CA_size, CA_size)
cel = np.piecewise(cel_rand, [cel_rand < cel_off, cel_rand >= cel_off], [0, 1])

print g_t, cel.sum(), ';',               

#fig = plt.figure()

#cel needs to become an "image"??
#after above plot declaration, need an "empty" image

#ims = []
#ims.append(plt.pcolor(cel))

#def animate(num, cel):
def trans():
    global g_t,cel
    rows = cel+np.roll(cel,1,0)+np.roll(cel,-1,0)
    cols = rows+np.roll(rows,1,1)+np.roll(rows,-1,1)
    
    a_cel = np.piecewise(cols, [cols < 3, cols == 3, cols == 4, cols > 4],[0,3,5,0])
    b_cel = cel + a_cel
    new_cel = np.piecewise(b_cel, [b_cel < 3, b_cel == 3, b_cel == 4, b_cel == 5, b_cel == 6, b_cel > 6],[0,1,1,0,1,0])

    g_t += 1

#    print g_t, new_cel.sum(), ';', 
    cel = new_cel
    return cel


files = []
#for i in range(generations): ims.append(plt.pcolor(trans(cel)))
for i in range(generations): 
    cur_cel = trans()
    print i,sum(sum(cur_cel)),';',
    imshow(cur_cel, cmap=plt.cm.gist_yarg, interpolation='nearest')
    fname = '_tmp%03d.png'%i
    savefig(fname)
    files.append(fname)


#for fname in files: os.remove(fname)
    
#im_ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=3000)
#im_ani.save('gol3001.mp4', writer=animation.FFMpegWriter(), fps=30, extra_args=['-vcodec', 'libx264'])

    
            
#ani = animation.FuncAnimation(fig, animate, frames=300, fargs=(cel), interval = 50, blit=True)
#plt.show()    
#im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000)
#im_ani.save('gol002.mp4', writer=animation.FFMpegWriter(), fps=30, extra_args=['-vcodec', 'libx264'])
#ani.save('double_pendulum.mp4', writer=animation.FFMpegWriter(), fps=30, extra_args=['-vcodec', 'libx264'])
