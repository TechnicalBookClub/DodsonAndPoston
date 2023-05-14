% D&P excercise I.2.6b example
%
% for the transformation "A", I'll use a 1/8 CCW rotation
% for the basis "B", I'll stretch the X axis by a factor of 2.

disp('I will label the bases, where the first label is the upper, or')
disp('"to" basis, and the second is the lower, or the "from" basis.')
disp('')
disp('Let A be a 1/8 CCW turn.  In the standard basis, this is:')
A_E_E = [1 -1; ...
         1  1] / sqrt(2)

disp('B is the "to" basis.  let''s stretch the x axis by a factor of 2')

b1_E = [2;0]
b2_E = [0;1]

B_E_E = [b1_E b2_E]

disp('Eqn 1 in my writeup is the change of basis from B to E:')

I_B_E = B_E_E

disp('for example, the consider the standard basis vector [1;1].  In')
disp('the B basis, this is [0.5,1]')

x_B = [0.5; 1]
x_E = [1  ; 1]

disp('x_E - I_B_E * x_B should be zero:')
x_E - I_B_E * x_B

disp('What is the 1/8 turn rotation matrix in basis B?')
I_E_B = inv(I_B_E);

disp('A_B_B = I_B_E * A_E_E * I_E_B')
A_B_B = I_B_E * A_E_E * I_E_B

disp('in multiples of sqrt(2), this is:')
A_B_B/sqrt(2)
