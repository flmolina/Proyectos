from tkinter import N, Entry, Tk, Frame,Button,Label, Toplevel, ttk
from zlib import DEF_BUF_SIZE
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from funciones import *


#configuracion grafica discreta
def ventana_discreta():
	fig, ax = plt.subplots(dpi=90, figsize=(7,5),facecolor='#9898F5')
	plt.title("Graficadora señales discretas",color='black',size=16, family="Arial")
	ax.set_xlabel("n", color='black')
	ax.set_ylabel("x[n]", color='black')
	ax.tick_params(direction='out', length=6, width=2, 
	colors='black',
    grid_color='r', grid_alpha=0.5)

	def discreta_1():
		plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
		plt.cla()
		a=eval(int.get())
		k = eval(k_v.get())
		t_0=eval(T_0v1.get())
		plot1=fig.add_subplot()	
		plot1.stem(x_n4(t_0,k,a)[0],x_n4(t_0,k,a)[1])
		Area2.draw()

	def discreta_2():
		a=eval(int.get())
		k = eval(k_v.get())
		t_0=eval(T_0v1.get())
		plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
		ax.set(xticks = [], yticks = [])	
		ax.axhline(linewidth=2, color='r')
		ax.axvline(linewidth=2, color='r')
		plt.cla()
		plot1=fig.add_subplot()	
		ax.set(xticks = [], yticks = [])
		plot1.stem(x_5n(t_0,k,a)[0],x_5n(t_0,k,a)[1])
		ax.set(xticks = [], yticks = [])
		Area2.draw()

	def discreta_3():
		plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
		plt.cla()
		a=eval(int.get())
		k = eval(k_v.get())
		t_0=eval(T_0v1.get())
		plot1=fig.add_subplot()	
		plot1.stem(x_6(t_0,k,a)[0],x_6(t_0,k,a)[1])
		Area2.draw()	
	ventana_discreta=Toplevel()
	ventana_discreta.title("graficadora discreta")
	ventana_discreta.geometry('642x650')
	ventana_discreta.wm_title('Graficadora Discreta')
	ventana_discreta.config(bg= "gray22")

	frame2 = Frame(ventana_discreta,  bg='gray22',bd=3)
	frame2.config(width="642", height="600")
	frame2.pack()

	Area2 = FigureCanvasTkAgg(fig, master = frame2)  # Crea el area de dibujo en Tkinter
	Area2.get_tk_widget().grid(column=0, row=0, columnspan=3, padx=5, pady =5)

	Button(frame2, text='x_4', width = 15, bg='DarkSeaGreen',fg='white', command=discreta_1).grid(column=0, row=1, pady =5)
	label = Label(frame2, width = 7)
	label.grid(column=1, row=1, pady =5)

	Button(frame2, text='x_5', width = 15, bg='DarkSeaGreen',fg='white', command= discreta_2).grid(column=0, row=2, pady =5)
	label = Label(frame2, width = 7)
	label.grid(column=1, row=1, pady =5)

	Button(frame2, text='x_6', width = 15, bg='DarkSeaGreen',fg='white', command=discreta_3).grid(column=0, row=3, pady =5)
	label = Label(frame2, width = 7)
	label.grid(column=1, row=1, pady =5)

	int=Entry(ventana_discreta)
	int.insert(0,0)
	int.place(x=291, y=581)
	int_label=Label(ventana_discreta,text="interpolacion")
	int_label.place(x=470, y=581)

	k_v = Entry(ventana_discreta)
	k_v.insert(0,1)
	k_v.place(x=291 ,y=471 )
	klabel=Label(ventana_discreta,text="factor de escalamiento")
	klabel.place(x=470,y=471)

	T_0v1= Entry(ventana_discreta)
	T_0v1.insert(0,0)
	T_0v1.place(x=291 ,y=530)
	tlabel=Label(ventana_discreta,text="factor de desplazamiento")
	tlabel.place(x=470,y=530)









##configuracion grafica continua

fig, ax = plt.subplots(dpi=90, figsize=(7,5),facecolor='#9898F5')
plt.title("Graficadora señales continuas",color='black',size=16, family="Arial")
ax.axhline(linewidth=2, color='r')
ax.axvline(linewidth=2, color='r')


ax.set_xlabel("t", color='black')
ax.set_ylabel("x(t)", color='black')





##Graficas continuas	




def x_1():

	plt.cla()
	ax.axhline(linewidth=2, color='r')
	ax.axvline(linewidth=2, color='r')
	
	k = eval(k_v.get())**-1
	a=eval(a_v.get())
	b=eval(b_v.get())
	c=eval(c_v.get())
	t_0=eval(T_0v.get())
	t = t=np.arange(-10,10,0.1) 
	line, = ax.plot(t*k, ((polinomial(a,b,c,t+t_0))), 
		color ='black', linestyle='solid')
	Area.draw()
	label.config(Text=k)
	line.set_ydata(0)


def x_2():
	
	k = eval(k_v.get())**-1
	t_0=eval(T_0v.get())
	plt.cla()
	ax.axhline(linewidth=2, color='r')
	ax.axvline(linewidth=2, color='r')
	t = t=np.arange(-10,10) 
	trix=tri(t_0)
	line, = ax.plot(t*k, ((trix)), 
		color ='black', linestyle='solid')
	Area.draw()
	label.config(Text=k)
	line.set_ydata(0)


def x_3():
	k = eval(k_v.get())**-1
	plt.cla()
	ax.axhline(linewidth=2, color='r')
	ax.axvline(linewidth=2, color='r')



	t = np.arange(-10,10, 0.01) 
	t_0=eval(T_0v.get())	

	line, = ax.plot(t*k, (np.exp(-1*abs(t+t_0))), 
		color ='b', linestyle='solid')
	Area.draw()

	label.config(Text=k)
	line.set_ydata(0)




	

	





root = Tk()
root.geometry('642x650')
root.wm_title('Graficadora continua')
root.config(bg= "gray22")

frame = Frame(root,  bg='gray22',bd=3)
frame.config(width="642", height="600")
frame.pack()

Area = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
Area.get_tk_widget().grid(column=0, row=0, columnspan=3, padx=5, pady =5)

##configuracion de los botones 
Button(frame, text='x_3', width = 15, bg='DarkSeaGreen',fg='white', command= x_3).grid(column=0, row=1, pady =5)
label = Label(frame, width = 7)
label.grid(column=1, row=1, pady =5)

Button(frame, text='x_2', width = 15, bg='DarkSeaGreen',fg='white', command= x_2).grid(column=0, row=2, pady =5)
label = Label(frame, width = 7)
label.grid(column=1, row=1, pady =5)

Button(frame, text='x_1', width = 15, bg='DarkSeaGreen',fg='white', command= x_1).grid(column=0, row=3, pady =5)
label = Label(frame, width = 7)
label.grid(column=1, row=1, pady =5)

Button(frame, text='Señales Discretas', width = 15, bg='SlateGray1',fg='Black',command=ventana_discreta ).grid(column=1, row=4, pady =5)
label = Label(frame, width = 7)
label.grid(column=1, row=1, pady =5)



 

k_v = Entry(root)
k_v.insert(0,0)
k_v.place(x=291 ,y=471 )
klabel=Label(root,text="factor de escalamiento")
klabel.place(x=470,y=471)

a_v = Entry(root)
a_v.insert(0,0)
a_v.place(x=580 ,y=170 )
alabel=Label(root,text="a")
alabel.place(x=600,y=150)

b_v = Entry(root)
b_v.insert(0,0)
b_v.place(x=580 ,y=220 )
blabel=Label(root,text="b")
blabel.place(x=600,y=200)

c_v = Entry(root)
c_v.insert(0,0)
c_v.place(x=580 ,y=270 )
clabel=Label(root,text="c")
clabel.place(x=600,y=250)

T_0v= Entry(root)
T_0v.insert(0,0)
T_0v.place(x=291 ,y=530)
tlabel=Label(root,text="factor de desplazamiento")
tlabel.place(x=470,y=530)
######################################################################

##Creacion de la ventana auxiliar, funciones discretas




root.mainloop()