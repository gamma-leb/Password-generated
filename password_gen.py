from distutils.core import run_setup
import random
from tkinter import *
import tk


run_screen= Tk()
run_screen.title("Password Generator")
run_screen.geometry("320x240+620+270")
run_screen.configure(bg="#d7dae2")
icon=PhotoImage(file="lock.gif")
run_screen.iconphoto(False,icon)

Label(text="password length :").place(x=120,y=20)
pass_length= Entry(width=8)
pass_length.place(x=150, y=50)

Label(text="By: G@MMA-LEB").place(x=200, y=220)

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*\/?"
password=StringVar()
use_for = lower_case + upper_case + number + symbols

def Gen():

    password.set("".join(random.sample(use_for, int(pass_length.get()))))

    Label(text="your generated password is:").place(x=100, y=130)
    Entry(textvariable=password, width=10).place(x=150, y=160)

Button(text="Generate", command=Gen).place(x=145, y=80)

run_screen.mainloop()