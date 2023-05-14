from numpy import *
from matplotlib.pyplot import *

pltsize = (4,3) # default plot size.  requires some monkeying with figure position.

close('all')

## Figure 1(i): numerator and denominator of the argument to the
## exponential part of f(x,y)
z = r_[1:3+1e-3:1e-3]
f1 = figure(1,figsize=pltsize)
clf()
plot(z,(z-2)**2/4)
grid('on')
plot(z,(z-2)**2 - 1)
xlabel(r'$y$ in units of $z$')
ylabel('components of $\log[g(z,y)]$')
legend(('numerator','denominator'))
f1.get_children()[1].set_position([.175,.16,.82,.83])
f1.text(0,1,'(i)',ha='left',va='top',fontfamily='serif')
savefig('Ex.VII.1.2_fig1.png')
xx = xlim()

## Figure 1(ii): the argument to the exponential part of f(x,y)
z = r_[1.1:2.9001:1e-3]
f2 = figure(2,figsize=pltsize)
clf(); plot(z,(z-2)**2/4/((z-2)**2 - 1))
grid('on')
xlabel(r'$y$ in units of $z$');
ylabel('log[g(z,y)]')
xlim(xx)
f2.get_children()[1].set_position([.165,.16,.82,.83])
f2.text(0,1,'(ii)',ha='left',va='top',fontfamily='serif')
savefig('Ex.VII.1.2_fig2.png')

## Figure 1(iii): the exponential part of f(x,y)
z = r_[1.01:2.9901:1e-3]
f3 = figure(3,figsize=pltsize)
clf();
plot(z,exp((z-2)**2/4/((z-2)**2 - 1)))
grid('on')
xlabel(r'$y$ in units of $z$');
ylabel('g(z,y)');
f3.get_children()[1].set_position([.15,.16,.82,.83])
f3.text(0,1,'(iii)',ha='left',va='top',fontfamily='serif')
savefig('Ex.VII.1.2_fig3.png')

## Figure 2: Neighborhoods of the zero map in L(T_xX;T_f(x)X')
x = np.array([-1,1])
tht = r_[0:2*pi+.001:.001] # for the circle
z = exp(1j * tht)
f4 = figure(4,figsize=(4.25,4))
clf()
plot(x, 1/2*(1-x)); # i = 1
plot(x, 2/2*(1-x)); # i = 2
grid('on')
axis('square')
axis([-1, 1, -1, 1]);
plot(z.real/sqrt(5),z.imag/sqrt(5),'--');
legend(('i=1','i=2','N([0,0])'));
xlabel(r'$A^x$')
ylabel(r'$A^y$')
f4.get_children()[1].set_position([.135,.115,.86,.86])
f4.get_children()[1].set_xticks([-1,-.5,0,.5,1])
f4.get_children()[1].set_yticks([-1,-.5,0,.5,1])
savefig('Ex.VII.1.2_fig4.png')

#show()
