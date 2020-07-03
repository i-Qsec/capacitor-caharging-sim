#Verwendete Bibliotheken
from tkinter import *
from matplotlib import pyplot as plt
import numpy as np

#Variablen zur Weiterverarbeitung in der Endgleichung 
Qmax = float

#Aktion des Button press
def show_values():
    print(a_R.get(), a_C.get(), a_U.get())
    
    #Qmax Berechnung durch Werte der Schieberegler
    Qmax = (a_C.get())*a_U.get()
    print(Qmax)
    
    #X- und Y- Achse -Y-Achse samt Gleichung
    x_t = np.arange(0, 5, 0.01)
    y_Q = float 
    y_Q = Qmax*(1-np.exp(-(1/a_R.get()*a_C.get())*x_t))
    print(y_Q)

    #Erstellung und Bennung der Diagramm Elemente
    plt.plot(x_t, y_Q)
    plt.xlabel("Zeit in s")
    plt.ylabel("Q")
    plt.title("Aufladungkurve")
    plt.show()

#Fenster erstellen 
test = Tk()
test.title("Aufladungkurve")

#Größe bei der Ausführung des Programms
test.minsize(width=400, height=200)

#Wiederstands Werte
a_R_Label = Label(test, text = "Wiederstand:")
a_R = Scale(test, from_ = 10, to = 100, orient = HORIZONTAL, length = 200)

#Farad Ladung des Kondensators
a_C_Label = Label(test, text = "mF/Millifarad:")
a_C = Scale(test, from_ = 10, to = 100, orient = HORIZONTAL, length = 200)
a_C.set(50)

#Spannung die auf dem Kondensator liegt
a_U_Label =Label(test, text = "Spannung auf dem Kondensator:")
a_U = Scale(test, from_ = 0, to = 10, orient = HORIZONTAL, length = 200)
a_U.set(10)

#Button der das Diagramm anzeigt
b = Button(test, text='Show', command=show_values)

#Position der GUI Elemte 
a_R_Label.pack()
a_R.pack()
a_C_Label.pack()
a_C.pack()
a_U_Label.pack()
a_U.pack()
b.pack()

test.mainloop()

