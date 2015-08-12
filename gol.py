#Game of Life
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

#import itertools
#import bases

CA_size = 32
generations = 128
g_t = 0

#random start with x_on% on
cel_off = 0.85
cel_rand = np.random.rand(CA_size, CA_size)
cel = np.piecewise(cel_rand, [cel_rand < cel_off, cel_rand >= cel_off], [0, 1])

print g_t, cel.sum(), ';', 
        
#seeded start
#cel = np.zeros([CA_size,CA_size])
#cel_loc = []
#for y in cel_loc:
#   cel[y] = 1

files = []

imshow(cel, cmap=plt.cm.gist_yarg, interpolation='nearest')
fname = '_tmp_start.png'
savefig(fname)
files.append(fname)


cur_cel = cel

#def updatefig(*args):
#    global CA_size, cel, g_t
for t in range(generations):
    rows = cel+np.roll(cel,1,0)+np.roll(cel,-1,0)
    cols = rows+np.roll(rows,1,1)+np.roll(rows,-1,1)
    
    a_cel = np.piecewise(cols, [cols < 3, cols == 3, cols == 4, cols > 4],[0,3,5,0])
    b_cel = cel + a_cel
    new_cel = np.piecewise(b_cel, [b_cel < 3, b_cel == 3, b_cel == 4, b_cel == 5, b_cel == 6, b_cel > 6],[0,1,1,0,1,0])

    g_t += 1
    print g_t, new_cel.sum(),';',

    imshow(new_cel, cmap=plt.cm.gist_yarg, interpolation='nearest')
    fname = '_tmp%03d.png'%t
    savefig(fname)
    files.append(fname)
    cel = new_cel
#    return im
 

# call mencoder 
#os.system("ffmpeg -r 2 -i _tmp%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p gol001.mp4")

# cleanup
#for fname in files: os.remove(fname)

        
                        
                      
# First set up the figure, the axis, and the plot element we want to animate
#fig = plt.figure()

#im = plt.imshow(cel, cmap=plt.cm.gist_yarg, interpolation='nearest')

#def updatefig(*args):
#    global x,y
#    x += np.pi / 15.
#    y += np.pi / 20.
#    im.set_array(f(x,y))
#    return im,
#im_ani = animation.ArtistAnimation(fig, im, interval=50)

#anim = animation.FuncAnimation(fig, updatefig, interval = 40, frames = generations)

#anim.save('gol.mp4', writer=animation.FFMpegWriter(), fps=30, extra_args=['-vcodec', 'libx264'])
#im_ani.save('gol.mp4', writer=animation.FFMpegWriter())

#plt.show()

# animation function.  This is called sequentially
#def animate(i):
#    x = np.linspace(0, 2, 1000)
#    y = np.sin(2 * np.pi * (x - 0.01 * i))
#    line.set_data(x, y)
#    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
#anim = animation.FuncAnimation(fig, animate, init_func=init,
#                               frames=200, interval=20, blit=True)
#anim = animation.FuncAnimation(fig, animate, init_func=init,
#                               frames=200, interval=20)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('gol.mp4', writer=animation.FFMpegWriter(), fps=30, extra_args=['-vcodec', 'libx264', '--verbose-debug'])

#plt.show()