import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as c
import matplotlib.animation as animation

#X=Pares de ranuras(1-15)pares (numero de ondas rectangulares)
#g= distancia del entrehierro(milimetros)
#N=numero de espiras
#intensidad de corriente
X=14
g=5
N=1000
I=2
I_m=I
f=60
k=30



#si se pasa restarle 360 grados
u = lambda t: np.heaviside(t,1) # se utilizara la señal escalon unitario
#como auxiliar para la construccion de señales rectangulares
theta=np.arange(-180.0,180,0.001) #Grados 

def Graf_B( X,g,N,I ):

    u = lambda t: np.heaviside(t,1)


    if X>=100 or X<=0: #numero de ranuras permitido
        print("error")
    else:
        mu=c.mu_0 #permeabilidad del vacio
        Angulo=45 #inicializacion de la variable
        pulso=0
        pulso_total=0
        delta=Angulo/X
        for i in range (1,X+1,1):
            A_B=(mu*N*I)/(2*g*10**-3)

            if i%2==0:
              pulso=(u(theta-Angulo-(delta*i)) + (-1*u(theta+Angulo-(delta*i))))*-1  
             
            else:
                pulso=(u(theta-Angulo+(delta*i)) + (-1*u(theta+Angulo+(delta*i))))*-1


            pulso*=A_B
            pulso_total+=pulso 

            plt.plot(theta,pulso)
            
        
        
    

        theta2=np.insert(theta,-1,theta+180)
        pulso_total2=np.insert(pulso_total,-1,-1*pulso_total)
        zeros=np.zeros(len(theta2))

        plt.plot(theta2,zeros,color="red")
        
        plt.axvline(x=0, ymin=-1, ymax=1,color="red")
        plt.plot(theta2,pulso_total2,color="purple")
    


        plt.show()
        return theta,pulso_total2

#Graf_B(X,g,N,I)

def animacion(I_m,f,k):
    #I_m es la amplitud de la corriente imcos(wt)
    #f es la frecuencia electrica
    #k contante de construccion
    theta2=np.arange(0,2/60,0.0001)
    w_0=2*np.pi*f

    F=(4/np.pi)*(k*3*N*I_m/2)*np.cos(theta2*w_0)#Amplitud de la onda rectangular
    
    fig, ax= plt.subplots()
    \
    def update_vector(frame):
        ax.clear()
        ax.set_ylim(-1*max(F), max(F))

        ax.plot(theta2,F*np.sin(frame))

    ani = animation.FuncAnimation(fig, update_vector, frames=np.arange(0,100,0.1), interval=1)
    plt.show()


animacion(I_m, f, k)






