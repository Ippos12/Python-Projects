from tkinter import *
e = Tk(className="Krishna's Calculator")
e.geometry("460x614")
e.resizable(bool(0),bool(0))
def insert(value):
    var.set(var.get() + value)
    eval(var.get())
def button(text, width, font, highlightbackground, x, y):
    tkinter_button = Button(e, text=text, width=width, command=lambda: insert(text), font=font, highlightbackground=highlightbackground)
    tkinter_button.place(x=x, y=y)
def clear():
    var.set(" ") 
def equals(vare):
    var.set(eval(vare))
helvetica = "Helvetica 50"   
arial = "Arial 50 bold"
purple = '#8533ff'
white = '#ffffff'
grey = '#737373'
var = StringVar()
label = Label(e, textvariable = var,bd=5,width=16, relief = SOLID, font = "Arial 50 ",bg="white", fg="black",activebackground="#bb99ff", height = 5,pady = 3)
label.place(x=0,y=0)
button(text = "-", width=4, font = helvetica, highlightbackground=purple, x = 344, y = 426)
button(text = "+", width=4, font = helvetica, highlightbackground=purple, x = 344, y = 488)
equal = Button(e, text = "=",width=4, command = lambda: equals(var.get()), font = helvetica, highlightbackground=purple)
equal.place(x = 344, y = 551)
aclear = Button(e, text = "AC",width=4, command = clear, font = helvetica ,highlightbackground=grey)
aclear.place(x = 0, y = 302)
square = Button(e, text = "^",width=4, command = lambda: insert("**"), font = helvetica,highlightbackground=grey)
square.place(x = 228, y = 301)
divide = Button(e, text = "÷",width=4, command = lambda: insert("/"), font = helvetica ,highlightbackground=purple)
divide.place(x = 344, y = 301)
multiply = Button(e, text = "x",width=4, command = lambda: insert("*"), font = helvetica ,highlightbackground=purple)
multiply.place(x = 344, y = 364)
delete = Button(e, text = "C",width=4, command=lambda: var.set(var.get()[:-1]), font = helvetica ,highlightbackground=grey)
delete.place(x = 114, y = 302)
for sym in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
    def Button1(text, x, y):
        Tkinterbutton = Button(e, text = text, width = 4, command=lambda: insert(text), font = arial, highlightbackground=white)
        Tkinterbutton.place(x=x, y=y)
Button1(text = ".", x = 228, y = 550)
button(text = "0", width = 8, font = arial, highlightbackground=white,x = 0, y = 550)
Button1(text = "1",  x = 0, y = 488)
Button1(text = "2", x = 114, y = 488)
Button1(text = "3", x = 228, y = 488)
Button1(text = "4", x = 0, y = 426)
Button1(text = "5", x = 114, y = 426)
Button1(text = "6", x = 228, y = 426)
Button1(text = "7", x = 0, y = 364)
Button1(text = "8", x = 114, y = 364)
Button1(text = "9", x = 228, y = 364)
e.mainloop()
