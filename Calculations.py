import numpy as np

L=np.array([50,50])                     
Qa=np.array([0.1,0.15])                  
B=np.array([0.3]*len(L))                 
RL=np.array([15.082, 14.986, 14.945])     
f=0.15;
N=len(RL);
shape=['trap']*len(L)
m=1.5
n=np.array([0.0275]*len(L))
D=np.array([0.3,0.35,0.4]) 

y=np.minimum(D[1:],D[:-1])-f
IL=RL-D
LLu=IL[:-1]+y
LLd=IL[1:]+y
S=(LLu-LLd)/L
T=B+2*m*D
a=(B+m*y)*y
p=B+2*np.sqrt(1+m**2)*y
r=a/p
Qc=(a*(r**0.66)*(S**0.5))/n
u=Qa/Qc
ch_a=LLu[:-1]-LLd[:-1]
ch_b=LLd[:-2]-LLu[1:-1]
Ar=(B+m*D)*D
Pr=B+2*np.sqrt(1+m**2)*D
Vol=np.sum((Ar[1:]+Ar[:-1])*L/2)
  
