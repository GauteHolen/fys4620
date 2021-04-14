# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:06:11 2021

@author: gaute
"""

import numpy as np

class BDriftSolver:
    
    
    
    
    def __init__(self,t_0,r_0,v_0,m,B_0,Bgrad,q):
        
        if len(v_0) != len(r_0):
            print("velocity and position must have same dimensions")
        
        self.t=t_0
        self.r=r_0
        self.v=v_0
        self.m=m
        self.B_0=B_0
        self.Bgrad=Bgrad
        self.q=q
        
    
    def get_B(self,r):
        Bd=self.Bgrad
        B=[0,0,0]
        
        #for i in range(len(r)):
        #    B[i]=self.B_0[i]+Bd[i]*r[i]
            
        B[2]=self.B_0[2]+r[1]*Bd[1]
    
        
        return B
            
    
    
    def velocity(self):
        return self.v
    
    def acceleration(self,r,v):
        B=self.get_B(r)
        
        return self.q*np.cross(v,B)/self.m
    
    def runEulerCromer(self,delta_t,t_n):
        
        positions=[self.r]
        x=[self.r[0]]
        y=[self.r[1]]
        z=[self.r[2]]
        t=[0]
        
        #Kinda stupid use of self here
        N=int(t_n/delta_t)
        
        x=np.empty((N,1))
        y=np.empty((N,1))
        z=np.empty((N,1))
        t=np.empty((N,1))
        
        r_current=self.r
        v_current=self.v
        
        
        for i in range(N):
            
            v_new=v_current+self.acceleration(r_current,v_current)*delta_t
            r_new=r_current+v_new*delta_t
            
            positions.append(r_new)
            v_current=v_new
            r_current=r_new
            
            self.t+=delta_t
            
            x[i]=(r_new[0])
            y[i]=(r_new[1])
            z[i]=(r_new[2])
            t[i]=(self.t)
            
        
        return x,y,z,t
    
    
    def runVerletVelocity(self,delta_t,t_n):
        x=[self.r[0]]
        y=[self.r[1]]
        z=[self.r[2]]
        t=[0]
        
        a_old=0
        
        
        while self.t<t_n:
            
            r_current=self.r
            v_current=self.v
            
            a_current=self.acceleration(r_current,v_current)
            r_new=r_current+v_current*delta_t+(1/6)*(4*a_current-a_old)*delta_t*delta_t
            
            
            
            
        
            self.t+=delta_t
            
            x.append(r_new[0])
            y.append(r_new[1])
            z.append(r_new[2])
            t.append(self.t)
        
        
        
        
        
        
        
        
        
    