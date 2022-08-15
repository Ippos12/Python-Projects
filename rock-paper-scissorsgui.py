#first lets import all the modules we will need
import random
from tkinter import *

#now let's create a window
e = Tk(className="Rock, paper, scissors")
e.geometry("800x400")
e.resizable(bool(0), bool(0))

#here we can define all the variables that we will need in the code 
var = StringVar()
purple = "#9999ff"
avenir = "Avenir 20"
blue = '#3366ff'
arial = "Arial 70 bold"
labeltext = "Welcome to Rock, Paper, Scissors. Pick your choice below."
userchoice = int
computerchoice = int

var.set("Let's play!")

#now we can condense our code a little bit by calling a function which would apply for each button
def Button1(text, x, command):
    Tkinterbutton = Button(e, text = text,width = 6,highlightbackground=blue,command = command,relief = RAISED, font = arial)
    Tkinterbutton.place(x=x, y = 150)

#and now we can do one which will be used for the bottom label, using a stringVar which we defined earlier
def elole(userchoice):
    computerchoice = random.randrange(1,3)
    if userchoice == computerchoice:
        var.set("It's a draw!")
    elif userchoice == 1 and computerchoice == 2:
        var.set("The computer traps your rock!")
    elif userchoice == 1 and computerchoice == 3:
        var.set("You obliterate the computer's scissors!")
    elif userchoice == 2 and computerchoice == 1:
        var.set("You smother the computer's rock with your paper!")
    elif userchoice == 2 and computerchoice == 3:
        var.set("The computer cuts your paper in half!")
    elif userchoice == 3 and computerchoice == 1:
        var.set("The computer smashes your scissors!")
    elif userchoice == 3 and computerchoice == 2:
        var.set("You slash the computer's paper into pieces!")

#and now finally we can create all the widgets we need (3 buttons, 2 labels) and close the window!
Button1(text = "R", x = 20, command = lambda: elole(1))
Button1(text = "P", x = 280, command = lambda: elole(2))
Button1(text = "S", x = 540, command = lambda: elole(3))
label = Label(e, text = labeltext,bd=2,width=63, relief = RAISED, font = avenir,bg=purple, fg="black", height = 4,pady = 3)
label.place(x=20,y=10)
label1 = Label(e, textvariable=var,bd=2,width=63, relief = SOLID, font = avenir,bg=purple, fg="black", height = 4,pady = 3)
label1.place(x=20,y=260)
e.mainloop()
#Have fun!