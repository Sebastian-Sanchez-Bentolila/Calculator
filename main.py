# @Author: Sebastian Sanchez Bentolila - https://github.com/Sebastian-Sanchez-Bentolila

#Modules
from tkinter import *
import os

indice = 0

class Calculadora():
    def __init__(self):
        #Window configuration
        self.ventana = Tk()
        self.ventana.geometry('500x600')
        self.ventana.title('Calculadora')
        self.RutaTrabajo = os.getcwd()
        self.ventana.iconbitmap('{}\\icons\\calculator.ico'.format(self.RutaTrabajo))
        self.ventana.resizable(0, 0)
        self.ventana.config(bg='light blue', cursor='spider')
        self.Widgets()
        
    def Widgets(self):
        #Buttons
        self.Boton0 = Button(self.ventana, text="0")
        self.Boton0.config(bg="black", 
                           fg="white",
                           relief="raised", 
                           justify="center",
                           font="Helvetica 18 bold", 
                           command= lambda: self.ClickBoton(0))
        self.Boton0.place(x=0, y=500, width=200, height=100)


        self.Boton1 = Button(self.ventana, text="1")
        self.Boton1.configure(bg="black", 
                              fg="white",
                              relief="raised", 
                              justify="center",
                              font="Helvetica 18 bold",
                              command= lambda: self.ClickBoton(1))
        self.Boton1.place(x=0, y=400, width=100, height=100)


        self.Boton2 = Button(self.ventana, text="2")
        self.Boton2.configure(bg="black", 
                              fg="white",
                              relief="raised", 
                              justify="center",
                              font="Helvetica 18 bold",
                              command= lambda: self.ClickBoton(2))
        self.Boton2.place(x=100, y=400, width=100, height=100)


        self.Boton3 = Button(self.ventana, text="3")
        self.Boton3.config(bg="black", 
                           fg="white",
                           relief="raised", 
                           justify="center",
                           font="Helvetica 18 bold",
                           command= lambda: self.ClickBoton(3))
        self.Boton3.place(x=200, y=400, width=100, height=100)


        self.Boton4 = Button(self.ventana, text="4")
        self.Boton4.config(bg="black", 
                           fg="white",
                           relief="raised", 
                           justify="center",
                           font="Helvetica 18 bold",
                           command= lambda: self.ClickBoton(4))
        self.Boton4.place(x=0, y=300, width=100, height=100)


        self.Boton5 = Button(self.ventana, text="5")
        self.Boton5.config(bg="black", 
                           fg="white",
                           relief="raised", 
                           justify="center",
                           font="Helvetica 18 bold",
                           command= lambda: self.ClickBoton(5))
        self.Boton5.place(x=100, y=300, width=100, height=100)


        self.Boton6 = Button(self.ventana, text="6")
        self.Boton6.config(bg="black", 
                           fg="white",
                           relief="raised", 
                           justify="center",
                           font="Helvetica 18 bold",
                           command= lambda: self.ClickBoton(6))
        self.Boton6.place(x=200, y=300, width=100, height=100)


        self.Boton7 = Button(self.ventana, text="7")
        self.Boton7.config(bg="black", 
                           fg="white",
                           relief="raised", 
                           justify="center",
                           font="Helvetica 18 bold",
                           command= lambda: self.ClickBoton(7))
        self.Boton7.place(x=0, y=200, width=100, height=100)


        self.Boton8 = Button(self.ventana, text="8")
        self.Boton8.config(bg="black", 
                           fg="white",
                           relief="raised", 
                           justify="center",
                           font="Helvetica 18 bold",
                           command= lambda: self.ClickBoton(8))
        self.Boton8.place(x=100, y=200, width=100, height=100)


        self.Boton9 = Button(self.ventana, text="9")
        self.Boton9.config(bg="black", 
                           fg="white",
                           relief="raised", 
                           justify="center",
                           font="Helvetica 18 bold",
                           command= lambda: self.ClickBoton(9))
        self.Boton9.place(x=200, y=200, width=100, height=100)


        self.BotonSuma = Button(self.ventana, text="+")
        self.BotonSuma.config(bg="black", 
                              fg="white",
                              relief="raised", 
                              justify="center",
                              font="Helvetica 18 bold",
                              command= lambda: self.ClickBoton("+"))
        self.BotonSuma.place(x=300, y=500, width=100, height=100)


        self.BotonResta = Button(self.ventana, text="-")
        self.BotonResta.config(bg="black", 
                               fg="white",
                               relief="raised", 
                               justify="center",
                               font="Helvetica 18 bold",
                               command= lambda: self.ClickBoton("-"))
        self.BotonResta.place(x=300, y=400, width=100, height=100)


        self.BotonMultiplicacion = Button(self.ventana, text="*")
        self.BotonMultiplicacion.config(bg="black", 
                                        fg="white",
                                        relief="raised", 
                                        justify="center",
                                        font="Helvetica 18 bold",
                                        command= lambda: self.ClickBoton("*"))
        self.BotonMultiplicacion.place(x=300, y=300, width=100, height=100)


        self.BotonDivision = Button(self.ventana, text="/")
        self.BotonDivision.config(bg="black", 
                                  fg="white",
                                  relief="raised", 
                                  justify="center",
                                  font="Helvetica 18 bold",
                                  command= lambda: self.ClickBoton("/"))
        self.BotonDivision.place(x=300, y=200, width=100, height=100)


        self.BotonPunto = Button(self.ventana, text=".")
        self.BotonPunto.config(bg="black", 
                               fg="white",
                               relief="raised", 
                               justify="center",
                               font="Helvetica 18 bold",
                               command= lambda: self.ClickBoton("."))
        self.BotonPunto.place(x=200, y=500, width=100, height=100)


        self.BotonIgual = Button(self.ventana, text="=")
        self.BotonIgual.config(bg="black", 
                               fg="white",
                               relief="raised", 
                               justify="center",
                               font="Helvetica 18 bold",
                               command= lambda: self.Ecuacion())
        self.BotonIgual.place(x=400, y=500, width=100, height=100)


        self.BotonAC = Button(self.ventana, text="AC")
        self.BotonAC.config(bg="black", 
                            fg="white",
                            relief="raised", 
                            justify="center",
                            font="Helvetica 18 bold",
                            command= lambda: self.Borrar())
        self.BotonAC.place(x=400, y=200, width=100, height=100)


        self.BotonON = Button(self.ventana, text="ON")
        self.BotonON.config(bg="black", 
                            fg="white",
                            relief="raised", 
                            justify="center",
                            font="Helvetica 18 bold",
                            command= lambda: self.Apagar())
        self.BotonON.place(x=400, y=100, width=100, height=100)


        self.BotonPI = Button(self.ventana, text="(")
        self.BotonPI.config(bg="black", 
                            fg="white",
                            relief="raised", 
                            justify="center",
                            font="Helvetica 18 bold",
                            command= lambda: self.ClickBoton("("))
        self.BotonPI.place(x=400, y=300, width=100, height=100)


        self.BotonPF = Button(self.ventana, text=")")
        self.BotonPF.config(bg="black", 
                            fg="white",
                            relief="raised", 
                            justify="center",
                            font="Helvetica 18 bold",
                            command= lambda: self.ClickBoton(")"))
        self.BotonPF.place(x=400, y=400, width=100, height=100)


        #Text (Entry)
        self.TextoResultado = Entry(self.ventana)
        self.TextoResultado.config(bg="light green", 
                                   fg="black",
                                   relief="groove", 
                                   justify="left",
                                   font="Helvetica 18 bold")
        self.TextoResultado.place(x=20, y=100, width=370, height=90)


        self.TextoEcuacion = Entry(self.ventana)
        self.TextoEcuacion.config(bg="white", 
                                  fg="black",
                                  relief="groove", 
                                  justify="left",
                                  font="Helvetica 18 bold")
        self.TextoEcuacion.place(x=20, y=10, width=460, height=80)   
        
    def RunApp(self):
        self.ventana.mainloop()

    #Functions
    def ClickBoton(self, valor):
        global indice
        self.TextoEcuacion.insert(indice, valor)
        indice += 1

    def Borrar(self):
        global indice
        self.TextoEcuacion.delete(0, END)
        indice = 0

    def Apagar(self):
        self.ventana.destroy()

    def Ecuacion(self):
        global indice
        self.ecuacion = self.TextoEcuacion.get()
        self.resultado = eval(self.ecuacion) #Solve the equation
        self.TextoEcuacion.delete(0, END)
        self.TextoResultado.delete(0, END)
        self.TextoResultado.insert(0, self.resultado)
        indice = 0
    

if __name__=='__main__':
    calculadora = Calculadora().RunApp()