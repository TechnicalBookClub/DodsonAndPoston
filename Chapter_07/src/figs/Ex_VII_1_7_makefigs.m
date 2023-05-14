

set(0,'defaultlinelinewidth',3);
set(0,'defaultaxesfontsize',18);
%set(0,'defaultlegendfontsize',18);

f = @(x)  2*x.^2.*sin(1./x) + x;

xx    = 1;
delta = xx/1e5;
x     = (-xx+delta/2):delta:(xx-delta/2);

figure(1)
subplot(311)
plot(x,f(x),'k:'); hold on;
plot(x,f(x)-x);
plot(x,f(x)-3*x); hold off;
grid on;
xlabel('x');
ylabel('see legend');
title('D&P VII.1.7b');
legend('f','f - x','f - 3x','location','northwest');

x=x/10;
subplot(312)
plot(x,f(x)-x);
ylabel('f - x');
grid on;

x=x/10;
subplot(313)
plot(x,(f(x) - x)); 
grid on;
xlabel('x');
ylabel('f - x');
