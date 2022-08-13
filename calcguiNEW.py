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
var = StringVar()
label = Label(e, textvariable = var,bd=5,width=16, relief = SOLID, font = "Arial 50 ",bg="white", fg="black",activebackground="#bb99ff", height = 5,pady = 3)
label.place(x=0,y=0)
button(text = "/", width=4, font = helvetica, highlightbackground='#8533ff', x = 344, y = 301)
button(text = "*", width=4, font = helvetica, highlightbackground='#8533ff', x = 344, y = 364)
button(text = "-", width=4, font = helvetica, highlightbackground='#8533ff', x = 344, y = 426)
button(text = "+", width=4, font = helvetica, highlightbackground='#8533ff', x = 344, y = 488)
equal = Button(e, text = "=",width=4, command = lambda: equals(var.get()), font = "Helvetica 50", highlightbackground='#8533ff')
equal.place(x = 344, y = 551)
aclear = Button(e, text = "AC",width=12, command = clear, font = "Helvetica 50",highlightbackground='#737373')
aclear.place(x = 0, y = 302)
button(text = ".", width=4, font = arial,highlightbackground='#ffffff', x = 228, y = 550)
button(text = "0", width = 8, font = arial,highlightbackground='#ffffff', x = 0, y = 550)
button(text = "1", width =4, font = arial,highlightbackground='#ffffff', x = 0, y = 488)
button(text = "2", width =4, font = arial,highlightbackground='#ffffff', x = 114, y = 488)
button(text = "3", width=4, font = arial,highlightbackground='#ffffff', x = 228, y = 488)
button(text = "4", width=4, font = arial,highlightbackground='#ffffff', x = 0, y = 426)
button(text = "5", width=4, font = arial,highlightbackground='#ffffff', x = 114, y = 426)
button(text = "6", width=4, font = arial,highlightbackground='#ffffff', x = 228, y = 426)
button(text = "7", width=4, font = arial ,highlightbackground='#ffffff', x = 0, y = 364)
button(text = "8", width=4, font = arial,highlightbackground='#ffffff', x = 114, y = 364)
button(text = "9", width=4, font = arial,highlightbackground='#ffffff', x = 228, y = 364)
e.mainloop()