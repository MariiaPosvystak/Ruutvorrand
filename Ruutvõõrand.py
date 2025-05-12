from tkinter import *
import math

def võrrand(a, b, c):
    a=int(sisetus.get())
    b=int(sisetus1.get())
    c=int(sisetus2.get())
    d=b**2 - 4*a*c
    D=math.sqrt(d)
    if d>0:
        x1=-(b)+D/2*a
        x2=-(b)-D/2*a
        pealkiri2.config(text="Решение\n"f"D = {d}\n"f"X1 = {x1}\n"f"X2 = {x2}",bg="yellow", font=("Arial",14), fg="black", width=25, height=5)
    elif d==0:
        x=-(b)/2*a
        pealkiri2.config(text="Решение\n"f"D = {d}\n"f"X1 = {x}",bg="yellow", font=("Arial",14), fg="black", width=25, height=5)
    else: 
        pealkiri2.config(text="Решения нет",bg="yellow", font=("Arial",14), fg="black", width=25, height=5)

def tuhista(event):
    sisetus.delete(0,END)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
aken=Tk()
aken.title("Квадратные уравнения")
aken.geometry("555x555")
aken.configure(bg="darkred")
aken.resizable(width=True, height=True)
pealkiri=Label(aken, text="Решение квадратного уравнения",bg="khaki", font=("Arial",18), fg="black")
text=Label(aken, text="x**2 + ",font=("Arial",14),bg="darkred", fg="black")
text1=Label(aken, text="x + ",font=("Arial",14),bg="darkred", fg="black")
text2=Label(aken, text=" = 0",font=("Arial",14),bg="darkred", fg="black")
nupp=Button(aken, text="Решить", bg="lightgreen", font=("Arial", 13),fg="brown", relief=RAISED)
nupp2=Button(aken, text="График", bg="lightgreen", font=("Arial", 13),fg="brown", relief=RAISED)#SUNKEN, RAISED,GROOVE, and RIDGE
sisetus=Entry(aken, bg="white", font=("Arial", 12), fg="black", width=3)
sisetus1=Entry(aken, bg="white", font=("Arial", 12), fg="black", width=3)
sisetus2=Entry(aken, bg="white", font=("Arial", 12), fg="black", width=3)
# sisetus.bind("<FocusIN>", tuhista)
# sisetus1.bind("<FocusIN>", tuhista)
# sisetus2.bind("<FocusIN>", tuhista)
nupp.bind("<Button>",võrrand )
pealkiri.grid(row=0, column=2, pady=20, columnspan=10)
sisetus.grid(row=1, column=1, pady=10, padx=5)
text.grid(row=1, column=2, pady=10)
sisetus1.grid(row=1, column=3, pady=10)
text1.grid(row=1, column=4, pady=10)
sisetus2.grid(row=1, column=5, pady=10)
text2.grid(row=1, column=6, pady=10)
nupp.grid(row=1, column=7, pady=10, padx=10)
nupp2.grid(row=1, column=8, pady=10)



pealkiri2=Label(aken, bg="yellow", text=f"Решение", font=("Arial",14), fg="black", width=25, height=5)
pealkiri2.grid(row=3, column=2, pady=20, columnspan=10)
aken.mainloop()
