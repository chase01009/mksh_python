import random as rd
import tkinter as tk

window = tk.Tk()
window.title("dice,exe")
window.geometry("200x200")

def dice(a):
    dice = ['a','b','c','d','e']
    for i in range(4):
        dice[i] = rd.randint(1,6)
    return dice[a]
def alldice():
    
    return dice(0), dice(1), dice(2), dice(3), dice(4)

#def total():
    #total = dice(0)+dice(1)+dice(2)+dice(3)+dice(4)
    #return total
def placea():
    aa = tk.Label(window, text=dice(0))
    aa.place(relx=0.3,rely=0.55)
    aa.config(text=dice(0))
    return aa
def placeb():
    ab = tk.Label(window, text=dice(1))
    ab.place(relx=0.4,rely=0.55)
    ab.config(text=dice(1))
    return ab
def placec():
    ac = tk.Label(window, text=dice(2))
    ac.place(relx=0.5,rely=0.55)
    ac.config(text=dice(2))
    return ac
def placed():
    ad = tk.Label(window, text=dice(3))
    ad.place(relx=0.6,rely=0.55)
    ad.config(text=dice(3))
    return ad
def placee():
    ae = tk.Label(window, text=dice(4))
    ae.place(relx=0.7,rely=0.55)
    ae.config(text=dice(4))
    return ae
def placetotal():
    atotal = tk.Label(window, text=total())
    atotal.place(relx=0.5,rely=0.45)
    atotal.config(text=total())
    return atotal
def allplaces():
    return placea(),placeb(),placec(),placed(),placee(),placetotal()

def click():
    alldice()
    allplaces()

btn = tk.Button(window, text="roll",font=("Arial",25,"bold"), command=click)
btn.pack(pady=20)
window.mainloop()
