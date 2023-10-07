from tkinter import *
import os

st = Tk()
st.title("Eteindre l'ordinateur")
st.geometry("500x500")
st.config(bg="grey")


def redemarer():
    os.system("shutdown /r /t 1")

def redemarer_temps():
    os.system("shutdown /r /t 20")

def deconnexion():
    os.system("shutdown -l")

def eteindre():
    os.system("shutdown /r /t 1")

re_button = Button(st, text="Rédemarer", font=('Times New Roman', 18, "bold"),
                   relief=RAISED, cursor = "plus", command=redemarer)
re_button.place(x=150, y=60, height = 50, width = 200)

ret_button = Button(st, text="Rédemarer Temps", font=('Times New Roman', 18, "bold"),
                    relief=RAISED, cursor = "plus", command=redemarer_temps)
ret_button.place(x=150, y=170, height = 50, width = 200)

lg_button = Button(st, text="Deconnexion", font=('Times New Roman', 18, "bold"),
                   relief=RAISED, cursor = "plus", command=deconnexion)
lg_button.place(x=150, y=270, height = 50, width = 200)

et_button = Button(st, text="Eteindre", font=('Times New Roman', 18, "bold"),
                   relief=RAISED, cursor = "plus", command=eteindre)
et_button.place(x=150, y=370, height = 50, width = 200)

st.mainloop()