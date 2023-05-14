from numpy import *
from matplotlib.pyplot import *

pltsize = (6,8)#(4,3) # default plot size.  requires some monkeying with figure position.


# for drawing boxes in fig.
boxx = np.array([-1, 1, 1, -1, -1])
boxy = np.array([-1, -1, 1, 1, -1])

def f(x):
    return 2*x**2*sin(1/x) + x

xx    = 1
delta = xx/1e5
x     = r_[-xx:xx:delta]+delta/2

clf()
f1 = figure(1, figsize=pltsize)
ax = f1.subplots(3,1)
ax[0].plot(x,f(x),'k:')
ax[0].plot(x,f(x)-x)
ax[0].plot(x,f(x)-3*x)
ax[0].grid('on')
ax[0].set_ylabel('see legend')
ax[0].set_title('D&P VII.1.7b')
ax[0].legend(('f','f - x','f - 3x'))

x = x/10
ax[1].ticklabel_format(axis='y',scilimits=(-1,1))
ax[1].plot(x,f(x)-x)
ax[1].grid('on')
ax[1].set_ylabel('f - x')
ax[0].plot(boxx*max(x), boxy*max(ax[1].get_ylim())*4, 'k', linewidth=.5)

x = x/5
ax[2].ticklabel_format(axis='y',scilimits=(-2,2))
ax[2].plot(x,f(x)-x)
ax[2].grid('on')
ax[2].set_xlabel('x')
ax[2].set_ylabel('f - x')
ax[1].plot(boxx*max(x), boxy*max(ax[2].get_ylim())*2, 'k', linewidth=.5)

ax[0].set_position([.15, .69, .8, .25])
ax[1].set_position([.15, .38, .8, .25])
ax[2].set_position([.15, .07, .8, .25])


savefig('Ex.VII.1.7b.png')

show()
