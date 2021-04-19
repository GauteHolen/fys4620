close all

a=1
b=1
B=1
C=1
psi=1

k = linspace(-1.5,1.5,1000);

w11 = (1/a).* sqrt(B*B+b*b*k.*k);
w12 = (-1/a).*sqrt(B*B+b*b*k.*k);

figure(1)
plot(k,w11,'b')
%xticks([-1, 0, 1])
%xticklabels({'-\beta', '0',  '\beta'})
%yticks([-1, 0, 1])
%yticklabels({'-1/\alpha', '0',  '1/\alpha'})
hold on
plot(k,w12,'b')
xlabel('k')
ylabel('\omega (k)')


figure(2)
w2i=(1/a).* sqrt(B*B+sqrt(B*B*B*B+4*b*b*b*b.*k.*k.*k.*k.*k.*k));
w2r=b*b.*k.*k.*k./w2i;
plot(k,w2i,'r')
hold on
plot(k,-1.*w2i,'r')
hold on
plot(k,w2r,'b')
hold on
plot(k,-1.*w2r,'b')
xlabel('k')
ylabel('\omega (k)')


figure(3)
w31 = (1/a).* sqrt(-b*b*k.*k.*k.*k+B*B);
hold on
w32 = -(1/a).* sqrt(-b*b*k.*k.*k.*k+B*B);
plot(k,w31,'b')
plot(k,w32,'b')
xlabel('k')
ylabel('\omega (k)')

figure(4)
w4 = (k./a).*(b*k.*k+C);
plot(k,w4)
xlabel('k')
ylabel('\omega (k)')

figure(5)
w5=(k./a).*(b*k.*k.*k+2*C*psi);
plot(k,w5)
xlabel('k')
ylabel('\omega (k)')





