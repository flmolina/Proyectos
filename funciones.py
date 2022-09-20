
from tkinter import N
import matplotlib.pyplot as plt
import numpy as np
import math as mt
def desplazar (x_n, t_0):
    if t_0>0:
     for i in range (0,t_0):
      x_n=np.append(x_n,0)
      x_n=np.delete(x_n,0)
    if t_0<0:
        t2=np.zeros(abs(t_0))
        x_n=np.hstack((t2,x_n))
        for i in range (0, abs(t_0)):
          x_n=np.delete(x_n,-1)
    if t_0==0:
        x_n=x_n
    return x_n

 ##Definiendo las funciones de interpolacion
def int_r(x_n,k,n):
    nm=[]
    x_n=x_n[::-1]
    x_nM=[]
    for i in range (0,len(x_n)*k):
        if i%k==0:
                x_nM.append (x_n[int(i/k)])
        else:
                x_nM.append(x_nM[-1])
    x_nM=x_nM[::-1]


    if n[0]<0:
        nm=np.arange((n[0]*k)-1*abs(k),((n[-1]*abs(k))))
        while len(nm)>len(x_nM):
            nm=np.delete(nm,-1)
        x_nM=np.vstack((nm,x_nM))
    
    return x_nM


def int_0(x_n,k,n):
    nm=[]
    x_nM=[]
    for i in range (0,len(x_n)*k):
        if i%k==0:
            x_nM.append (x_n[int(i/k)])
        else :
            x_nM.append (0)
    if n[0]<0:
        nm=np.arange((n[0]*k)-1*abs(k),((n[-1]*abs(k))))
        while len(nm)>len(x_nM):
            nm=np.delete(nm,-1)
        x_nM=np.vstack((nm,x_nM))

    return x_nM

def int_L(x_n,k,n):
    Ln=len(n)
    nM=np.arange (n[0]*k, (n[-1]*k)+1)
    x_nM=np.arange(0, len(nM)) 
    z=1
    for i in range (0,Ln-1):
        x_nM[z]=x_n[i]
        for j in range (0, k-1):
            dif=(x_n[i])-(x_n[i-1])
            x_nM[k+1]=x_n[i]+((j/k)*dif)
            z=z+1
        z=z+1
    x_nM=np.vstack((nM,x_nM))
    return x_nM





##Hasta ahora solo diezmado
def Diez_inter (x_n, k,a,n):
    k=abs(k)
    x_nM=[]
    if a==0:
        L_xn=len(x_n)
        for i in range (0,L_xn):
            if i % abs(k) ==0:
                x_nM.append(x_n[i])
        n0=np.arange(0,(len(x_n)/abs(k)))
        x_nM=np.vstack((n0,x_nM))
    
    if a==1:
        x_nM=int_0(x_n,k,n)
        if n[0]==0:
            n0=np.arange(0,(len(x_nM)))
            x_nM=np.vstack((n0,x_nM))
    if a==2:
        x_nM=int_r(x_n,k,n)
        if n[0]==0:
            n0=np.arange(0,(len(x_nM)))
            x_nM=np.vstack((n0,x_nM))

    if a==3:
        x_nM=int_L(x_n,k,n)

    return x_nM 

##recordar siempre pedir el intervalo a graficar  para funciones 
#continuas o que no tengan t definido
#Funcion 1
def polinomial (a,b,c,t):
    return a*t**2+b*t+c
## para los continuos se dejara explicito dentro de la funcion cuanto se rodara e interpolara
##Funcion 2
def tri(t_0):
    t = t=np.arange(-10,10) 
    for i in range(0,len(t)):
        if abs(t[i])<1:
         t[i]=1-abs(t[i])
        elif abs(t[i])>=1:
            t[i]=0
    if t_0>0:
     for i in range (0,t_0):
      t=np.append(t,0)
      t=np.delete(t,0)
    if t_0<0:
        t2=np.zeros(abs(t_0))
        t=np.hstack((t2,t))
        for i in range (0, abs(t_0)):
          t=np.delete(t,-1)

    return t

##uncion 3:
def euler(t):
    return np.exp(-1*abs(t))

#funcion 4: CORREGIDO
def x_n4 (t_0,k,a):
    x_4=[-6,0,1,2,6,5,1,0,4,7,3,-2,3,6]
    if k <0:
        x_4=x_4[::-1]
    n=np.arange(0,len(x_4))
    x_4=desplazar(x_4,t_0)
    x_4=Diez_inter(x_4,k,a,n)







    return x_4

##funcion 5
def x_5n(t_0,k,a):
    x_5=[]
    k2=k
    k=abs(k)
    n=np.arange (-10,11)
    for i in range (0, len(n)):
        if n[i]>9 or n[i]<-8:
            x_5.append(0)
        if n[i]>=-8 and n[i]<=-4:
            x_5.append(-2)
        if n[i]>=-3 and n[i] <=2:
            x_5.append(2*n[i])
        if n[i] >=3 and n[i]<9:
            x_5.append (9/n[i])    
    if  k2 <0:
         x_5=x_5[::-1]
    if a ==0:
        x_5.append(0)
    x_5=desplazar(x_5,t_0)
    if a >=1:
        x_5=Diez_inter(x_5,k,a,n)
    if a==0:
        x_5=Diez_inter(x_5,k,a,n)[1]  ##Ajuste del vector de tiempo para diezmado
        if k%2==0:
            n=np.arange((mt.floor(n[0]/k)), mt.ceil(((n[-1])/k)+1))
        if k==3:
            n=np.arange((mt.floor(n[0]/k)), mt.ceil(((n[-1])/k)))
        if k==1:
            n=np.arange((mt.floor(n[0]/k)), mt.ceil(((n[-1])/k))+1)
        x_5=np.vstack((n,x_5))
    return x_5



def x_6(t_0,k,a):
    n=np.arange(-10,10, dtype=float)
    x_6=[]
    k2=k
    for i in range (0,len(n)):
        if n[i]>=-5 and n[i]<=0:
            x_6.append(2**n[i])
        if n[i]>0 and n[i]<7:
            x_6.append((3/2)**n[i])
        else :
            x_6.append (0)
    
    while len(n)<len(x_6):
        x_6=np.delete(x_6,-1)
    
    if  k2 <0:
        x_6=x_6[::-1]
    x_6=desplazar(x_6,t_0)
    if a >=1:
        n=np.asarray(n,dtype=int)
        x_6=np.asarray(x_6,dtype=int)
        x_6=Diez_inter(x_6,k,a,n)
    if a==0:
        x_6=Diez_inter(x_6,k,a,n)[1]  ##Ajuste del vector de tiempo para diezmado
        if k%2==0:
            n=np.arange((mt.floor(n[0]/k)), mt.ceil(((n[-1])/k)))
        if k==3:
            n=np.arange((mt.floor(n[0]/k)), mt.ceil(((n[-1])/k)))
        if k==1:
            n=np.arange((mt.floor(n[0]/k)), mt.ceil(((n[-1])/k))+1)
        x_6=np.vstack((n,x_6))
    return x_6



##sta aca las funciones que se van a usar durante el laboratorio``
