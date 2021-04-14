# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:00:13 2021

@author: gaute
"""

import matplotlib.pyplot as plt

from BDriftSolver import BDriftSolver as Solver

t_0=0
m=1
r_0=[0,0,0]
v_0=[0,1,0]
B_grad=[0,10,0]
B_0=[0,0,10]
q=-1

delta_t = 0.0001
t_n = 3



solver = Solver(t_0,r_0,v_0,m,B_0,B_grad,q)
x,y,z,t = solver.runEulerCromer(delta_t,t_n)

#print(x)
#print(y)
#print(z)
#print(t)

plt.plot(x,y)

#x,y,z,t = solver.runVerletVelocity(delta_t,t_n)
#plt.plot(x,y)



