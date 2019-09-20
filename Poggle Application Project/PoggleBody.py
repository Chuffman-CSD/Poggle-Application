#!/usr/bin/python3

import tkinter as tk
import random
import socket



#Frame{ root(tk.Tk(){  } objects{  }, __init__(self) { ... } }

class Frame:

    objects = {}
    
    def __init__(self,Name="Guest"):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.name = Name
        self.objects["NG"] =  str(random.randint(1000,10000))
        self.objects["GT"] = self.objects["NG"]
        print (self.objects["GT"])
        self.objects["GT"] = self.objects["NG"]
        self.objects["WelcomeLabel"] = tk.Label(master=self.root,text="Welcome "+Name + "#"+self.objects["GT"]+"!")
        self.objects["WelcomeLabel"].grid()
        self.objects["TextField"]= tk.Entry(master=self.root)
        self.objects["TextField"].grid()
