import random as rd
import tkinter as tk

window = tk.Tk()
window.title("dice,exe")
window.geometry("200x200")

def dicea():
    a = rd.randint(1,6)
    return a
def diceb():
    b = rd.randint(1,6)
    return b
def dicec():
    c = rd.randint(1,6)
    return c
def diced():
    d = rd.randint(1,6)
    return d
def dicee():
    e = rd.randint(1,6)
    return e
def dice():
    return dicea(),diceb(),dicec(),diced(),dicee()

def total():
    total = dicea()+diceb()+dicec()+diced()+dicee()
    return total
def placea():
    aa = tk.Label(window, text=dicea())
    aa.place(relx=0.3,rely=0.55)
    aa.config(text=dicea())
    return aa
def placeb():
    ab = tk.Label(window, text=diceb())
    ab.place(relx=0.4,rely=0.55)
    ab.config(text=diceb())
    return ab
def placec():
    ac = tk.Label(window, text=dicec())
    ac.place(relx=0.5,rely=0.55)
    ac.config(text=dicec())
    return ac
def placed():
    ad = tk.Label(window, text=diced())
    ad.place(relx=0.6,rely=0.55)
    ad.config(text=diced())
    return ad
def placee():
    ae = tk.Label(window, text=dicee())
    ae.place(relx=0.7,rely=0.55)
    ae.config(text=dicee())
    return ae
def placetotal():
    atotal = tk.Label(window, text=total())
    atotal.place(relx=0.5,rely=0.45)
    atotal.config(text=total())
    return atotal
def allplaces():
    return placea(),placeb(),placec(),placed(),placee(),placetotal()

def click():
    dice()
    allplaces()

btn = tk.Button(window, text="roll",font=("Arial",25,"bold"), command=click)
btn.pack(pady=20)
window.mainloop()