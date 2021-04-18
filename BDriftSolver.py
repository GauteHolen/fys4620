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
        
        #offsets starting position with r_g
        r_g = self.m*self.v[1]/(-1*self.q*self.B_0[2])
        
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
        r_current[0]=r_g
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
    
    
    def runGyrocenterApprox(self,delta_t,t_n):
        
        K_perp=0.5*self.m*self.v[1]**2
        
        BgradB2 = np.cross(self.B_0,self.Bgrad)/(self.B_0[2]**2)
        
        
        v_drift = BgradB2*K_perp/(self.q*self.B_0[2])
        
        
        N=int(t_n/delta_t)
        x=np.empty((N,1))
        y=np.empty((N,1))
        z=np.empty((N,1))
        t=np.empty((N,1))
        x_drift=0
        tt=0
        for i in range(N):
            tt+=delta_t
            
            x[i]=x_drift
            x_drift+=v_drift[0]*delta_t
            y[i]=0
            z[i]=0
            t[i]=tt
        
        return x,y,z,t
        
        
        
        
        
        
        
    