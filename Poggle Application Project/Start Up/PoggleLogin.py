#!/usr/bin/python3
import tkinter as tk
import PoggleBody as pf
import random

IN_USE_USERNAMES = ["admin","test","1","2",""]

DEFAULT = ("Times New Roman", 15)

COLORS = ["black","yellow"]

color_mode = 0

class Login(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        # -- informations label --
        self.infoLabel = tk.Label(self, text=" \n Welcome, please login to proceed or register \n", font = DEFAULT, bg = "black", fg = "white")
        self.infoLabel.grid(column = 0, row = 1)
        #self.infoLabel.grid()

        # -- username text label --
        self.usernameLabel = tk.Label(self, text="Enter a username:",font = DEFAULT, bg = "black", fg = "white")
        self.usernameLabel.grid(column = 0, row = 2)
        #self.usernameLabel.grid()

        # -- username text box --
        self.userNameBox = tk.Entry(self, font = DEFAULT)
        self.userNameBox.grid(column = 0, row = 3)
        #self.userNameBox.grid()

        # -- login button --
        self.loginButton = tk.Button(self, text="Continue",command=self.proceed,bg="Green",font = DEFAULT,)
        self.loginButton.grid(column = 0, row = 4)
        #self.loginButton.grid()

        # -- Username in use label --
        self.infoLabel = tk.Label(self,text="\n Error: Username is in use! \n",font = DEFAULT, bg = "black", fg = "black")
        self.infoLabel.grid(column = 0, row = 5)
        #self.infoLabel.grid()

    def proceed(self):
        global color_mode
        global error_count
        if self.userNameBox.get() in IN_USE_USERNAMES and color_mode == 0:
            self.infoLabel.configure(text="\n Error: Username is in use!\n", font = DEFAULT, fg = COLORS[1])
        elif self.userNameBox.get() not in IN_USE_USERNAMES:
            characterCount = self.userNameBox.get()
            if len(characterCount) > 12:
                self.infoLabel.configure(text="\n Error: Username is too long!\n", font = DEFAULT, fg = COLORS[1])
                print("Error: Username too long!")
            elif len(characterCount) < 4:
                self.infoLabel.configure(text="\n Error: Username is too short!\n", font = DEFAULT, fg = COLORS[1]) #Character count will be 20 characters
                print("Error: Username too short!")
            else:
                frame = pf.Frame(Name=self.userNameBox.get())
                root.destroy()
        else:
            print("\nSomething went wrong..\n")

root = tk.Tk()
root.title("Login")

root.geometry("380x240")

frame_login = Login()
frame_login.configure(background="black")
frame_login.grid(row = 0, column = 0)
                 
root.mainloop()

