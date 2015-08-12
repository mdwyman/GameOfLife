"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
plt.rcParams['animation.ffmpeg_path'] = '/Applications/ffmpeg'

CA_size = 32
generations = 128
g_t = 0

#random start with x_on% on
#cel_off = 0.85
#cel_rand = np.random.rand(CA_size, CA_size)
#cel = np.piecewise(cel_rand, [cel_rand < cel_off, cel_rand >= cel_off], [0, 1])

#cel = []

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
#ax = plt.axes(xlim=(0, CA_size-1), ylim=(0, CA_size-1))
ca, = plt.imshow(np.empty([CA_size, CA_size]), cmap=plt.cm.gist_yarg, interpolation='nearest')
#line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    ca.set_data([])
    return ca,

# animation function.  This is called sequentially
def animate(i, CA_size):
    global g_t,cel
    if i == 0:
        cel_off = 0.85
        cel_rand = np.random.rand(CA_size, CA_size)
        cel = np.piecewise(cel_rand, [cel_rand < cel_off, cel_rand >= cel_off], [0, 1])
    rows = cel+np.roll(cel,1,0)+np.roll(cel,-1,0)
    cols = rows+np.roll(rows,1,1)+np.roll(rows,-1,1)
    
    a_cel = np.piecewise(cols, [cols < 3, cols == 3, cols == 4, cols > 4],[0,3,5,0])
    b_cel = cel + a_cel
    new_cel = np.piecewise(b_cel, [b_cel < 3, b_cel == 3, b_cel == 4, b_cel == 5, b_cel == 6, b_cel > 6],[0,1,1,0,1,0])

    g_t += 1

    print g_t, new_cel.sum(), ';',     
    ca.set_data(new_cel)
    return ca,

# call the animator.  blit=True means only re-draw the parts that have changed.
#anim = animation.FuncAnimation(fig, animate, init_func=init,
#                               frames=200, interval=20, blit=True)

#anim = animation.FuncAnimation(fig, animate, init_func=init,
#                               frames=200, interval=20)

anim = animation.FuncAnimation(fig, animate, fargs = (CA_size),
                               frames=generations, interval=20)


# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', writer=animation.FFMpegWriter(), fps=30, extra_args=['-vcodec', 'libx264', '--verbose-debug'])

plt.show()