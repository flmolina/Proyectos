
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as c
#X=Pares de ranuras(1-15)pares (numero de ondas rectangulares)
#g= distancia del entrehierro(milimetros)
#N=numero de espiras
#intensidad de corriente

#si se pasa restarle 360 grados
u = lambda t: np.heaviside(t,1) # se utilizara la señal escalon unitario
#como auxiliar para la construccion de señales rectangulares
theta=np.arange(-200,600,0.001) #Grados 

def Graf_B( X,g,N,I ):

    u = lambda t: np.heaviside(t,1)


    if X>=40 or X<=0: #numero de ranuras permitido
        print("error")
    else:


        mu=c.mu_0 #permeabilidad del vacio
        Angulo=90 #inicializacion de la variable
        pulso=0
        pulso_total=0
        delta=90/X
        for i in range (1,X+1,1):
            A_B=(mu*N*I)/(2*g*10**-3)

            if i%2==0:
             pulso=(u(theta-Angulo-(delta*i)) + (-1*u(theta+Angulo-(delta*i))))*-1  -(
                 (u(theta-180-(delta*i)))                                         )
            else:
                pulso=(u(theta-Angulo+(delta*i)) + (-1*u(theta+Angulo+(delta*i))))*-1 -(
                 (u(theta-(180)-(delta*i)))                                         )

            pulso*=A_B
            pulso_total+=pulso
            
            plt.plot(theta,pulso)
        
        plt.show()
        plt.plot(theta,pulso_total)
        plt.show()

Graf_B(1,5,200,0.5)
