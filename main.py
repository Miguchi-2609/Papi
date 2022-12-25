from logging import root
from tkinter import *
from tkinter import messagebox
from tkinter.tix import LabelEntry
import webbrowser
import time
import threading
import glob
import os
from update_check import isUpToDate


window = Tk()
window.title("Papy")
window.iconbitmap(r'C:\Users\mitem\Desktop\code\logotest.ico')
label = Label(window, text="Bonjour papy!", font = ( "Arial Bold" , 30 ), fg ="white", bg = "black")
label.pack(side=LEFT)
label = Label(window, text="comment va", font = ( "Arial Bold" , 30 ), fg ="white", bg = "black")
label.pack()




button = Button(text="Retourner sur Windows 11", command=quit)
button.pack(side=BOTTOM)


from update_check import isUpToDate

if isUpToDate(__file__, "https://raw.githubusercontent.com/username/repo/myProgram.py") == False:
   doSomething()



 
window.attributes("-fullscreen", True)
window.configure(bg='black')
window.mainloop()
exit(0)
