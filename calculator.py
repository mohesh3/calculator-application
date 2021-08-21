from tkinter import *
import parser
from math import factorial
from math import sqrt
import tkinter.font as font

window = Tk()
window.geometry("425x248")
window.configure(background='black')
window.title("calculator by Mohesh")
#window.iconbitmap("icon.ico")

i = 0
# Receives the digit as parameter and display it on the input field
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1
 
# Calculate function scans the string to evaluates and display it
def calculate(*args):
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
 
# Function which takes operator as input and displays it on the input field
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length
 
#Function to clear the input field 
def clear_all(*args):
    display.delete(0,END)
 
#Function which works like backspace
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

#Function to calculate the factorial and display it
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"please enter a integer to get answer")
#function to calculate the square root of the given function
def sqrte():
    entire_string = display.get()
    try:
        result = sqrt(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"please enter a integer to get answer")

#----------------  application and button design  ----------------------#

#adding the input field
display = Entry(window)
display.grid(row=1,columnspan=6,ipadx=60,ipady=30,sticky=N+E+W+S)
display.configure(background='#0D0D0D',foreground='white')
myfont= font.Font(family='Helvetica', size=20, weight='bold')
display['font']=myfont
display.grid()
window.bind("<Return>",calculate)
window.bind("c",clear_all)

#adding number buttons to the Calculator

Button(window,text="1",command = lambda :get_variables(1)).grid(row=2,column=0,sticky=N+S+E+W)
Button(window,text=" 2",command = lambda :get_variables(2)).grid(row=2,column=1,sticky=N+S+E+W)
Button(window,text=" 3",command = lambda :get_variables(3)).grid(row=2,column=2, sticky=N+S+E+W)
 
Button(window,text="4",command = lambda :get_variables(4)).grid(row=3,column=0, sticky=N+S+E+W)
Button(window,text=" 5",command = lambda :get_variables(5)).grid(row=3,column=1, sticky=N+S+E+W)
Button(window,text=" 6",command = lambda :get_variables(6)).grid(row=3,column=2, sticky=N+S+E+W)
 
Button(window,text="7",command = lambda :get_variables(7)).grid(row=4,column=0, sticky=N+S+E+W)
Button(window,text=" 8",command = lambda :get_variables(8)).grid(row=4,column=1, sticky=N+S+E+W)
Button(window,text=" 9",command = lambda :get_variables(9)).grid(row=4,column=2, sticky=N+S+E+W)
 
#adding other buttons to the calculator
Button(window,text="AC",command=lambda :clear_all()).grid(row=5,column=0, sticky=N+S+E+W)
Button(window,text=" 0",command = lambda :get_variables(0)).grid(row=5,column=1, sticky=N+S+E+W)
Button(window,text=" .",command=lambda :get_variables(".")).grid(row=5, column=2, sticky=N+S+E+W)
 
Button(window,text="+",command= lambda :get_operation("+")).grid(row=2,column=3, sticky=N+S+E+W)
Button(window,text="-",command= lambda :get_operation("-")).grid(row=3,column=3, sticky=N+S+E+W)
Button(window,text="*",command= lambda :get_operation("*")).grid(row=4,column=3, sticky=N+S+E+W)
Button(window,text="/",command= lambda :get_operation("/")).grid(row=5,column=3, sticky=N+S+E+W)
 
# adding new operations
Button(window,text="pi",command= lambda :get_operation("*3.14")).grid(row=2,column=4, sticky=N+S+E+W)
Button(window,text="%_div",command= lambda :get_operation("%")).grid(row=3,column=4, sticky=N+S+E+W)
Button(window,text="(",command= lambda :get_operation("(")).grid(row=4,column=4, sticky=N+S+E+W)
Button(window,text="exp",command= lambda :get_operation("**")).grid(row=5,column=4, sticky=N+S+E+W)
 
Button(window,text="<--",command= lambda :undo()).grid(row=2,column=5, sticky=N+S+E+W)
Button(window,text="x!", command= lambda: fact()).grid(row=3,column=5, sticky=N+S+E+W)
Button(window,text="sqrt", command= lambda: sqrte()).grid(row=6,column=5, sticky=N+S+E+W)
Button(window,text=")",command= lambda :get_operation(")")).grid(row=4,column=5, sticky=N+S+E+W)
Button(window,text="^2",command= lambda :get_operation("**2")).grid(row=5,column=5, sticky=N+S+E+W)
Button(window,text="=",fg='#E21717',activeforeground='green',command= lambda :calculate()).grid(row=6,columnspan=5,sticky=N+S+E+W)
window.mainloop()
