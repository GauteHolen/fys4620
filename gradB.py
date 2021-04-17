# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:00:13 2021

@author: gaute
"""

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from BDriftSolver import BDriftSolver as Solver

t_0=0
#Initial position and velocity
r_0=[0,0,0]
v_0=[0,10**(5),0]

#Magnetic field gradient and magnetic field given in Tesla
B_grad=[0,5*10**(-4),0]
B_0=[0,0,50*10**(-6)]




#Mass in KG
m_e=9.10938356*10**(-31)
m_p=1.6726219*10**(-27)
#Particle charge given in Columb
q_e=-1.602176634*10**(-19)
q_p=1.602176634*10**(-19)

q=q_e
m=m_e
#Time step
t_n = 5*2*3.14159*m/(abs(q)*B_0[2]) #Formula for 5 gyroperiods
delta_t=t_n*10**(-4)





solver = Solver(t_0,r_0,v_0,m,B_0,B_grad,q)
x,y,z,t = solver.runEulerCromer(delta_t,t_n)
x_gc,y_gc,z_gc,t_gc = solver.runGyrocenterApprox(delta_t,t_n)


r_g = m*v_0[1]/(abs(q)*B_0[2])
print("theoretical gyroradius: ",r_g)
print("simulated gyroradius: ", max(y))


if q>1:
    kind='Proton'
else:
    kind='Electron'

legend=['Euler Cromer','Gyrocenter Approx']

s=str('$v_0=$'+str(format(v_0[1],'.3E'))+'m/s'+
      ', $B_{grad y} =$'+str(format(B_grad[1],'.3E'))+'T/m'+
      ', $B_0 = $'+str(format(B_0[2],'.3E')))+'T'

fig1, ax1 = plt.subplots()
ax1 = plt.axes(projection='3d')
ax1.scatter3D(x,t,y,s=0.5)
ax1.scatter3D(x_gc,t_gc,y_gc,s=0.5)
ax1.set_xlabel('X [m]')
ax1.set_ylabel('time [s]')
ax1.set_zlabel('Y [m]')
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax1.legend(legend, loc='best')
ax1.set_title(kind+' trajectory on XY plane in time with '+'\n'+s+'\n')
plt.tight_layout()
#ax1.annotate('$v_0=$'+str(v_0[2])+'m/s')

fig2, ax2 = plt.subplots()
ax2.plot(x,y)
ax2.plot(x_gc,y_gc)
ax2.set_xlabel('X [m]')
ax2.set_ylabel('Y [m]')
ax2.legend(legend, loc='upper left')

ax2.set_title(kind+' trajectory on XY plane with '+'\n'+s)
plt.tight_layout()

