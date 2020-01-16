#!/usr/bin/python3

import tkinter as tk
import random
import socket
import time
from datetime import *


DEFAULT = ("Times New Roman",15)
username = ""
Messages = []
adminCommands = ["\\help"]
amountOfMessages = 0
sentMessages = []
nowDate = datetime.now()

#Frame{ root(tk.Tk(){  } objects{  }, __init__(self) { ... } }

class Frame:

    objects = {}
    
    def __init__(self,Name="Guest"):
        global DEFAULT
        global Messages
        global username 
        self.root = tk.Tk()
        self.root.title("Poggle: Chat Service")
        self.root.geometry("750x500")
        #self.root.grid_columnconfigure(0, weight = 1)
        self.name = Name

        #--NewFrame--
        self.objects["NewFrame"]=tk.Frame(master=self.root)
        self.objects["NewFrame"].grid(column=0,row=2,columnspan=10)

        
        self.objects["NG"] =  str(random.randint(1000,10000))
        self.objects["GT"] = self.objects["NG"]
        print(self.objects["GT"])
        self.objects["GT"] = self.objects["NG"]
        self.objects["SpacerLabel"] = tk.Label(master=self.root,text="          \n")
        self.objects["SpacerLabel"].grid(column=0)
        self.objects["WelcomeLabel"] = tk.Label(master=self.root,text="\nWelcome "+Name + "#"+self.objects["GT"]+"!\n",font=DEFAULT)
        self.objects["WelcomeLabel"].grid(column=0,row=0)
        self.objects["TextField"]=tk.Entry(master=self.root, width = 75,font=DEFAULT)
        self.objects["TextField"].grid(column=0,row=1)

        username=(Name+"#"+self.objects["GT"])

        #inside 'NewFrame'
        self.objects["lbl_spacer1"]=tk.Label(self.objects["NewFrame"],text="  ",font=DEFAULT)
        self.objects["lbl_spacer1"].grid(column=1,row=0)

        #inside 'NewFrame'
        self.objects["SendButton"]=tk.Button(self.objects["NewFrame"],text="Send",bg="Green",font=DEFAULT,command=self.send)
        self.objects["SendButton"].grid(column=1,row=1)

        #inside 'NewFrame'
        self.objects["ClearButton"]=tk.Button(self.objects["NewFrame"],text="Clear",bg="Green",font=DEFAULT,command = self.clear_text)
        self.objects["ClearButton"].grid(column=2,row=1)

        #inside 'NewFrame'
        self.objects["ExitButton"]=tk.Button(self.objects["NewFrame"],text="Exit",bg="Green",font=DEFAULT,command = self.exit_program)
        self.objects["ExitButton"].grid(column=3,row=1)

        #inside 'NewFrame'
        self.objects["lbl_spacer2"]=tk.Label(self.objects["NewFrame"],text="  \n\n",font=DEFAULT)
        self.objects["lbl_spacer2"].grid(column=4,row=1)

        #inside 'NewFrame'
        self.objects["MessagesInfoLabel"]=tk.Label(master=self.objects["NewFrame"],text="Global Messages:\n",font=DEFAULT)
        self.objects["MessagesInfoLabel"].grid(column=1,row=2,columnspan=3)
        
        #inside 'NewFrame'
        self.objects["RecieveMessages"]=tk.Label(self.objects["NewFrame"],text="Message: ",font=DEFAULT,width=35)
        self.objects["RecieveMessages"].grid(column=1,row=3,columnspan=3)
        
    def clear_text(self):
        self.objects["TextField"].delete(0,"end")
    def exit_program(self):
        self.objects["WelcomeLabel"].configure(text="DICSONNECTED")
        print("Disconnected, restart program to continue.")
        quit()
    def send(self):
        global amountOfMessages
        global Messages
        global username
        global amountOfMessages
        global sentMessages
        amountOfMessages += 1
        characterCount = self.objects["TextField"].get()
        print(len(characterCount))
        #if len(characterCount) >
        self.objects["RecieveMessages"].configure(text="")
        commandSearch = self.objects["TextField"].get()
        Messages.append(self.objects["TextField"].get())
        print(commandSearch)
        if commandSearch == "\help":
            print("\help, used!")
            self.objects["TextField"].delete(0,"end")
            self.objects["RecieveMessages"].configure(text="Message: ")
            print("\n-Admin Commands-\n")
            print("cmd: \loadmsglist - Loads a list of all recorded messages")
        elif commandSearch == "\loadmsglist":
            print("\nLoading all previous messages, please wait.\n")
            for message in sentMessages:
                print(message)
            print("\nSuccess, all messages have been loaded!\n")
            self.objects["TextField"].delete(0,"end")
            self.objects["RecieveMessages"].configure(text="Message: ")
        else:
            if commandSearch == "":
                localMessage = "Error, Blank Field"
                Messages = []
                #Debugging - print("Str - LocalMessage: ",localMessage)
                #Debugging - print("List - Messages",Messages)
                self.objects["RecieveMessages"].configure(text=str(username)+": "+"Blank.. \n")
                #sentMessage.append(str(amountOfMessages," ") + str(localMessage))
                sentMessages.append("Date/Time:"+str(nowDate)+" User:"+str(username)+" Message:"+str(localMessage))
                self.objects["TextField"].delete(0,"end")
            else:
                localMessage = str(Messages[-1])
                Messages = []
                #Debugging - print("Str - LocalMessage: ",localMessage)
                #Debugging - print("List - Messages",Messages)
                self.objects["RecieveMessages"].configure(text=str(username)+": "+str(localMessage)+"\n")
                #sentMessage.append(str(amountOfMessages," ") + str(localMessage))
                sentMessages.append("Date/Time:"+str(nowDate)+" User:"+str(username)+" Message:"+str(localMessage))
                self.objects["TextField"].delete(0,"end")
