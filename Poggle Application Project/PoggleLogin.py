#!/usr/bin/python3
import tkinter as root
import PythonFile as pf
import random

window = root.Tk()

window.title("Login")

window.geometry("325x250")

def proceed():
    x = 1
    if userNameBox.get() == (""):
        frame = pf.Frame()
        window.destroy()
    else:
        frame = pf.Frame(userNameBox.get())
        window.destroy()

# -- informations label --
infoLabel = root.Label(text=" \n Welcome, please login to proceed or register \n")
infoLabel.grid()
# -- username text label --
usernameLabel = root.Label(text="Enter a username:")
usernameLabel.grid(column=0, row=1)
# -- username text box --():
userNameBox = root.Entry()
userNameBox.grid(column=0,row=2)
# -- login button --
loginButton = root.Button(text="Continue",command=proceed)
loginButton.grid(column=0,row=7)
# -- Username in use label --
infoLabel = root.Label(text="\n Error: Username is in use! \n")
infoLabel.grid()

window.mainloop()

