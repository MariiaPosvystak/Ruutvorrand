import math
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
def lahendus(event):
    a=sisestus.get()
    b=sisestus1.get()
    c=sisestus2.get()
    if not a or not b or not c:
        if not a:
            sisestus.config(bg="red", font=("Arial",12), fg="black",width=3)
        if not b:
            sisestus1.config(bg="red", font=("Arial",12), fg="black",width=3)
        if not c:
            sisestus2.config(bg="red", font=("Arial",12), fg="black",width=3)
        pealkiri5.config(text="Palun sisestage kõik kordajad!", bg="red",  font=("Arial", 13), fg="black", width=20, height=5)
        return
    try:
        arv1=int(a)
        arv2=int(b)
        arv3=int(c)
    except:
        pealkiri5.config(text="Sisestage ainult täisarvud!", bg="red", font=("Arial", 13), fg="black", width=20, height=5)
        return
    sisestus.config( bg="lightblue", font=("Arial",12), fg="green",width=3)
    sisestus1.config( bg="lightblue", font=("Arial",12), fg="green",width=3)
    sisestus2.config( bg="lightblue", font=("Arial",12), fg="green",width=3)
    D=arv2**2-4*arv1*arv3
    if D>0:
        d=math.sqrt(D)
        x1=round((-arv2+d)/(2*arv1),2)
        x2=round((-arv2-d)/(2*arv1),2)
        pealkiri5.config(text=f"D = {D}\n x1 = {x1} \n x2 = {x2}", bg="lightpink",  font=("Arial", 13), fg="black", width=20, height=5)
    elif D==0:
        x=round(-arv2/2*arv1,2)
        pealkiri5.config(text=f"D = {D}\n x = {x}", bg="lightblue",  font=("Arial", 13), fg="black", width=20, height=5)
    else:
        pealkiri5.config(text="Lahendusi ei ole!", bg="lightgreen",  font=("Arial", 13), fg="black", width=20, height=5)

def graafik(event):
    arv1=int(sisestus.get())
    arv2=int(sisestus1.get())
    arv3=int(sisestus2.get())
    x=np.arange(-11,12,1)
    y=arv1*x**2+arv2*x+arv3
    plt.figure(facecolor='lightblue')
    plt.title("Graafik")
    plt.xlabel("x telg")
    plt.ylabel("y telg")
    plt.grid(True)
    plt.plot(x,y, color='yellow', linestyle='-', marker='D',
    markersize=8, label="Joonisejoon")
    plt.show()


aken=Tk()
aken.title("Teema 8")
aken.geometry("500x500")
aken.configure(bg="white")
aken.resizable(width=False, height=False)
pealkiri=Label(aken, text="Ruutvõrrandi lahendamine", bg="lightblue", font=("Arial", 16), fg="green")
nupp=Button(aken, text="Lahenda!", bg="green", font=("Arial", 12), fg="black", relief=RAISED)
nupp.bind("<Button-1>", lahendus)
nupp1=Button(aken, text="Graafik", bg="green", font=("Arial", 12), fg="black", relief=RAISED)#RAISED, GROOVE, RIDGE,SUNKEN
nupp1.bind("<Button-1>", graafik)
sisestus=Entry(aken, bg="lightblue", font=("Arial",12), fg="green",width=3)
pealkiri2=Label(aken, text="x**2+", bg="white", font=("Arial", 16), fg="green")
sisestus1=Entry(aken, bg="lightblue", font=("Arial",12), fg="green",width=3)
pealkiri3=Label(aken, text="x+", bg="white", font=("Arial", 16), fg="green")
sisestus2=Entry(aken, bg="lightblue", font=("Arial",12), fg="green",width=3)
pealkiri4=Label(aken, text="=0", bg="white", font=("Arial", 16), fg="green")
pealkiri5=Label(aken, text="Lahendus", bg="yellow", font=("Arial", 13), fg="black", width=20, height=5)

pealkiri.grid(row=0, column=2, pady=10, columnspan=10)

sisestus.grid(row=1, column=1, pady=10)
pealkiri2.grid(row=1, column=2, pady=10)
sisestus1.grid(row=1, column=3,pady=10)
pealkiri3.grid(row=1, column=4, pady=10)
sisestus2.grid(row=1, column=5, pady=10)
pealkiri4.grid(row=1, column=6, pady=10)

nupp.grid(row=1, column=7, pady=10)
nupp1.grid(row=1, column=8, pady=10)

pealkiri5.grid(row=2, column=2, pady=10, columnspan=10)

aken.mainloop()