from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt 
from numpy import pi,sin,cos,tan,linspace
from matplotlib.pyplot import  plot,show,xlim,ylim,xticks, legend, figure,subplot
N=100
def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará..")
    ventana_principal.destroy()


#Funcion lineal
def calcularlineal(m,b,x):
  return int(m.get())*x+int(b.get())
def mostrar_lineal():
  y= calcularlineal(m,b,x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion lineal: y=mx+b")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 

def funcion_lineal():
  
  # etiqueta para m
  lb_x = Label(frame_operaciones, text = "m =  ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=20, width=115, height=30)
  # entry para m
  entry_x = Entry(frame_operaciones, textvariable=m)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="black")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # etiqueta para b
  lb_x = Label(frame_operaciones, text = "b =  ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=60, width=115, height=30)
  # entry para b
  entry_x = Entry(frame_operaciones, textvariable=b)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="black")
  entry_x.focus_set()
  entry_x.place(x=135,y=60,width=115, height=30)

  # etiqueta para c
  lb_x = Label(frame_operaciones, text = "   ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=100, width=115, height=30)

  # entry para c
  lb_x = Label(frame_operaciones, text = "     ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=135,y=100,width=115, height=30)

  # etiqueta para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=250, y=20, width=115, height=30)
  # entry para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=350,y=20,width=115, height=30)
  
  #boton cuadratica
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=funcion_cuadratica)
  bt_cuadratica.place(x=50,y=150, width=100, height=30)

# Funcion cuadratica
def calcular_cuadratica(a,x,b,c):
  return int(a.get())*x**2+int(b.get())*x+int(c.get())

def funcion_cuadratica():
  # etiqueta para a
  lb_x = Label(frame_operaciones, text = "a =  ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=20, width=115, height=30)
  # entry para a
  entry_x = Entry(frame_operaciones, textvariable=a)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="black")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # etiqueta para b
  lb_x = Label(frame_operaciones, text = "b =  ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=60, width=115, height=30)
  # entry para b
  entry_x = Entry(frame_operaciones, textvariable=b)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="black")
  entry_x.focus_set()
  entry_x.place(x=135,y=60,width=115, height=30)
  # etiqueta para c
  lb_x = Label(frame_operaciones, text = "c =  ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=100, width=115, height=30)
  # entry para c
  entry_x = Entry(frame_operaciones, textvariable=c)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="black")
  entry_x.focus_set()
  entry_x.place(x=135,y=100,width=115, height=30)
  # etiqueta para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=250, y=20, width=115, height=30)
  # entry para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=350,y=20,width=115, height=30)
  
  #boton calcular
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=mostrar_cuadratica)
  bt_cuadratica.place(x=50,y=150, width=100, height=30)

def mostrar_cuadratica():
  y=calcular_cuadratica(a,x,b,c)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion cuadratica: y=ax**2+bx+c")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 
def calcular_cubica(a,x,b,c,d):
    return int(a.get())*x**3+int(b.get())*x*2+int(c.get())*x+int(d.get())
def mostrar_cubica():
  y=calcular_cubica(a,x,b,c,d)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion cubica: y=ax*3+bx*2+cx+d")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 

def funcion_cubica():
  
  lb_x = Label(frame_operaciones, text = "a =  ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=20, width=115, height=30)
  # entry para a
  entry_x = Entry(frame_operaciones, textvariable=a)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="black")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # etiqueta para b
  lb_x = Label(frame_operaciones, text = "b =  ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=60, width=115, height=30)
  #entry para b
  entry_x = Entry(frame_operaciones, textvariable=b)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="black")
  entry_x.focus_set()
  entry_x.place(x=135,y=60,width=115, height=30)
  # etiqueta para c
  lb_x = Label(frame_operaciones, text = "c =  ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=100, width=115, height=30)
  # entry para c
  entry_x = Entry(frame_operaciones, textvariable=c)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="black")
  entry_x.focus_set()
  entry_x.place(x=135,y=100,width=115, height=30)

  # etiqueta para d
  lb_x = Label(frame_operaciones, text = "d =  ")
  lb_x.config(bg="grey79", fg="black", font=("Arial",16))
  lb_x.place(x=250, y=20, width=115, height=30)
  # entry para d
  entry_x = Entry(frame_operaciones, textvariable=d)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="black")
  entry_x.focus_set()
  entry_x.place(x=350,y=20,width=115, height=30)

  #boton calcular
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=mostrar_cubica)
  bt_cuadratica.place(x=50,y=150, width=100, height=30)

def calcular_expotencial(x,a):
  return int(a.get())**x
def funcion_expotencial():
  
  lb_x = Label(frame_operaciones, text = "a =  ")
  lb_x.config(bg="gre70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=20, width=115, height=30)
  # entry para a
  entry_x = Entry(frame_operaciones, textvariable=a)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="black")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # etiqueta para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="grey70grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=60, width=115, height=30)
  #entry para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=135,y=60,width=115, height=30)
  # etiqueta para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=100, width=115, height=30)
  # entry para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=135,y=100,width=115, height=30)
  # etiqueta para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=250, y=20, width=115, height=30)
  # entry para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=350,y=20,width=115, height=30)
  #boton calcular
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=mostrar_expotencial)
  bt_cuadratica.place(x=50,y=150, width=100, height=30)
def mostrar_expotencial():
  y=calcular_expotencial(x,a)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion cubica: y=ax*3+bx*2+cx+d")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 
  
# funcion logaritmo
def funcion_logaritmica(x):
  return np.log(x)
def mostrar_logaritmo():
  y=funcion_logaritmica(x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion Logaritmica Y=log(x)")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show()
def funcion_trigonometrica():
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=20, width=115, height=30)
  # entry para a
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=135,y=20,width=115, height=30)
  
  # etiqueta para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=60, width=115, height=30)
  #entry para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=135,y=60,width=115, height=30)
  # etiqueta para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=10, y=100, width=115, height=30)
  # entry para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=135,y=100,width=115, height=30)
  # etiqueta para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=250, y=20, width=115, height=30)
  # entry para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=350,y=20,width=115, height=30)
  #boton calcular
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="grey70", fg="black", font=("Arial",16))
  lb_x.place(x=50,y=150, width=100, height=30)
  
  bt_seno = Button(frame_operaciones, text="sen(x)", command=mostrar_seno)
  bt_seno.place(x=50,y=80, width=100, height=30)

  bt_coseno = Button(frame_operaciones, text="cos(x)", command=mostrar_coseno)
  bt_coseno.place(x=200,y=80, width=100, height=30)

  bt_tangente= Button(frame_operaciones, text="tan(x)", command=mostrar_tangente)
  bt_tangente.place(x=350,y=80, width=100, height=30)
  return bt_coseno.destroy
  
def funcion_trigonometricaseno(x):
  return sin(x)
def mostrar_seno():
  y=funcion_trigonometricaseno(x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion sen(x)")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show()
  
def funcion_trigonometricacoseno(cos,x):
  return cos(x)
def mostrar_coseno():
  
  x=linspace(-pi,2*pi,num=N)
  y=funcion_trigonometricacoseno(cos,x)
  legend(loc="upper left")
  plot(x,y, label="coseno")
  ylim(-1,1)
  plt.title("Funcion y=coseno(x)")
  plt.grid()
  plt.axhline(y=0 ,color="r")
  plt.axvline(x=0, color="r")
  xticks([-pi,-pi/2,0,pi/2,pi],[r'$-\pi$',r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
  show()
  
def funcion_trigonometricatangente(tan,x):
  return tan(x)
def mostrar_tangente():
 
  N=100
  #processing- grafica
  x=linspace(-pi,2*pi,num=N)
  y=funcion_trigonometricatangente(tan,x)
  legend(loc="upper left")
  plot(x,y, label="tangente")
  ylim(-10,10)
  plt.title("Funcion y=tan(x)")
  plt.grid()
  plt.axhline(y=0 ,color="r")
  plt.axvline(x=0, color="r")
  xticks([-pi,-pi/2,0,pi/2,pi],[r'$-\pi$',r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
  show()
  
    
ventana_principal = Tk()
c= StringVar()
a = StringVar()
b = StringVar()
m = StringVar()
d = StringVar()
x= np.linspace(-10,10, num=N)


# titulo de la ventana
ventana_principal.title("Funciones")

# tamañan de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg= "black")

# etiqueta para el titulo de la app
titulo = Label(ventana_principal, text= "FUNCIONES")
titulo.config(bg="black", fg="white", font=("Arial",18))
titulo.place(x=50,y=10, width=400, height=40)
# boton lineal
bt_lineal = Button(ventana_principal, text="Lineal", command=funcion_lineal)
bt_lineal.place(x=50,y=80, width=100, height=30)

#boton cuadratica
bt_cuadratica = Button(ventana_principal, text="Cuadratica", command=funcion_cuadratica)
bt_cuadratica.place(x=200,y=80, width=100, height=30)

#boton cubica
bt_cubica= Button(ventana_principal, text="Cubica", command=funcion_cubica)
bt_cubica.place(x=350,y=80, width=100, height=30)

#boton expotencial
bt_expotencial= Button(ventana_principal, text="Expotencial", command=funcion_expotencial)
bt_expotencial.place(x=50,y=180, width=100, height=30)

#funcion logaritmo
bt_logaritmo= Button(ventana_principal, text="logaritmica", command=mostrar_logaritmo)
bt_logaritmo.place(x=200,y=180, width=100, height=30)

#funcion trigonometrica
bt_trigonometrica= Button(ventana_principal, text="trigonometrica", command=funcion_trigonometrica)
bt_trigonometrica.place(x=350,y=180, width=100, height=30)

# ------------------------
# frame operaciones
# ------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="grey70", width=480, height=190)
frame_operaciones.place(x=10,y=300)

ventana_principal.mainloop()