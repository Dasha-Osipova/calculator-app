from tkinter import *
from tkinter.messagebox import *

#global history valriable
hist = ""

def history():
    showinfo('recent history', message = hist)

def makemenu(win):
    top = Menu(win)    
    
    # creates pulldown menu
    file = Menu(top)
    file.add_command(label='History', command=history, underline=0)
    top.add_cascade(label='File', menu=file, underline=0)    

    win.config(menu=top)
        

# a tkinter app window called 'root' is created
root = Tk()
root.title('Calculator')
makemenu(root)

# a global variable that holds the entire string typed by the user
equa = ""

equation = StringVar()

# the value of equation is passed over to the Label widget through the textvariable option
calculation = Label(root, textvariable = equation, height = 7)

# updating the value of equation 
equation.set("Enter your equation:")

calculation.grid(columnspan = 4)

def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def EqualPress():
    global equa
    global hist
    hist = equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""

def clear():
    global equa
    global hist
    equa = ""
    hist = ""
    equation.set("")

Button0 = Button(root, text = "0", width = 6, height = 3, command = lambda: btnPress(0))
Button0.grid(row = 4, column = 1)

Button1 = Button(root, text = "1", width = 6, height = 3, command = lambda: btnPress(1))
Button1.grid(row = 1, column = 0)

Button2 = Button(root, text = "2", width = 6, height = 3, command = lambda: btnPress(2))
Button2.grid(row = 1, column = 1)

Button3 = Button(root, text = "3", width = 6, height = 3, command = lambda: btnPress(3))
Button3.grid(row = 1, column = 2)

Button4 = Button(root, text = "4", width = 6, height = 3, command = lambda: btnPress(4))
Button4.grid(row = 2, column = 0)

Button5 = Button(root, text = "5", width = 6, height = 3, command = lambda: btnPress(5))
Button5.grid(row = 2, column = 1)

Button6= Button(root, text = "6", width = 6, height = 3, command = lambda: btnPress(6))
Button6.grid(row = 2, column = 2)

Button7 = Button(root, text = "7", width = 6, height = 3, command = lambda: btnPress(7))
Button7.grid(row = 3, column = 0)

Button8 = Button(root, text = "8", width = 6, height = 3, command = lambda: btnPress(8))
Button8.grid(row = 3, column = 1)

Button9 = Button(root, text = "9", width = 6, height = 3, command = lambda: btnPress(9))
Button9.grid(row = 3, column = 2)

Plus = Button(root, text = "+", width = 6, height = 3, command = lambda: btnPress("+"))
Plus.grid(row = 1, column = 3)

Minus = Button(root, text = "-", width = 6, height = 3, command = lambda: btnPress("-"))
Minus.grid(row = 2, column = 3)

Multiply = Button(root, text = "*", width = 6, height = 3, command = lambda: btnPress("*"))
Multiply.grid(row = 3, column = 3)

Divide = Button(root, text = "/", width = 6, height = 3, command = lambda: btnPress("/"))
Divide.grid(row = 4, column = 3)

Equal = Button(root, text = "=", width = 6, height = 3, command = EqualPress)
Equal.grid(row = 4, column = 2)

Clear = Button(root, text = "C", width = 6, height = 3, command = clear)
Clear.grid(row = 4, column = 0)

# starts the tkinter event loop
root.mainloop()
