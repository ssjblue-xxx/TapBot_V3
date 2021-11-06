from tkinter import *
from tkinter import Label
import pyautogui, time

print("TapBot, le meilleur programme pour tricher sur tout site de dactylographie")
print("")
print("TAPBOT ON TOP")

TapBot = Tk()
TapBot.config(background="black")
TapBot.geometry("475x250")
TapBot.title("TapBot V3 Linux")

l = Label(TapBot, font=("Arial",40), text="TapBot V3", bg="black", fg="White")
l.place(x=100, y=30)

l1 = Label(TapBot, font=("Arial",15), text="texte", bg="black", fg="White")
l1.place(x=10, y=120)

l2 = Label(TapBot, font=("Arial",15), text="intervale", bg="black", fg="White")
l2.place(x=10, y=150)

l22 = Label(TapBot, font=("Arial",10), text="record acctuelle : 8146 mot par minute", bg="black", fg="white")
l22.place(x=100, y=180)

words2 = Entry(TapBot, width=35)
words2.place(x=100, y=120)

speed1 = Entry(TapBot, width=35)
speed1.place(x=100, y=150)

def yes():
    words = words2.get()
    speed = speed1.get()
    time.sleep(5)
    pyautogui.typewrite(words, interval=speed)

def help():
    helpwin = Tk()
    helpwin.title("utilisation")
    helpwin.config(background="black")
    l3 = Label(helpwin, text="1. marquer le texte voulu, 2. mettre l'intervale (intervale rec. : 0.15) et appuier sur commencer et allez sur l'exercise voulu (assez rapidement car j'ai mit un temp d'attente de 5 secondes)", fg="white", bg="black")
    l3.pack()
    helpwin.mainloop()

def creds():
    creds = Tk()
    creds.config(background="black")
    creds.title("remerciments")
    l5 = Label(creds, text="merci a 4lpn#7925 (moi xd) pour avoir rendu ce projet possible et a botti le canard#1020 pour etre le premier testeur de TabBot", fg="white", bg="black")
    l5.pack()
    creds.mainloop()

def bug():
    bug = Tk()
    bug.config(background="black")
    bug.title("signaler un bug")
    l0 = Label(bug, text="si vous avez trouve un bug sur la version mac ou linux, merci de le signaler a 4lpn#7925 sur discord, si vous avez trouve un bug sur la version windows merci de le signaler a botti le canard#1020", fg="white", bg="black")
    l0.pack()
    bug.mainloop()

b = Button(TapBot, text="commencer", command=yes)
b.place(x=10, y=200)

b1 = Button(TapBot, text="utilisation", command=help)
b1.place(x=120, y=200)

b2 = Button(TapBot, text="remerciements", command=creds)
b2.place(x=220, y=200)

b3 = Button(TapBot, text="signaler un bug", command=bug)
b3.place(x=350, y=200)

TapBot.mainloop()
