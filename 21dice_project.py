#21dice_project
#create in 2025-05-27

import random as rd
import tkinter as tk

x = int(0)
y = int(0)
A = [x,y]
a_a = 0
def r_r():
    for i in range(2):
        A[i] = rd.randint(1,6)
def amount(a):
    A[a]
    return A[a]
def t_a():
    t_a = A[0]+A[1]
    global a_a
    a_a = t_a + a_a
    t_a = "%02d" % t_a
    return t_a
def click():
    return r_r()

window = tk.Tk()
window.title("21_dice")
window.geometry("200x200")

def place_symbles():
    place_plus = tk.Label(window, text='+',font=("Bernard MT Condensed",15,"bold"))
    place_plus.place(relx=0.3,rely=0.55)
    place_equles = tk.Label(window, text='=',font=("Bernard MT Condensed",15,"bold"))
    place_equles.place(relx=0.5,rely=0.55)
def place(a):
    places = tk.Label(window, text=amount(a),font=("Bernard MT Condensed",15,"bold"))
    places.place(relx=0.2+a*0.2,rely=0.55)
    places.config(text=amount(a))
    return places
def p_t():
    atotal = tk.Label(window, text=t_a(),font=("Bodoni MT Black",25,"bold"))
    atotal.place(relx=0.6,rely=0.5)
    atotal.config(text=t_a())
    return atotal
def a_p():
    return place(0),place(1),p_t(),place_symbles()

def click():
    r_r()
    a_p()
    print(a_a)

btn1 = tk.Button(window, text="roll",font=("Arial",25,"bold"), command=click)
btn1.pack(pady=20)

window.mainloop()