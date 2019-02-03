'''
Created on 3 Feb 2019

@author: Devel
'''
from tkinter import *

expression = ""

def press(num):
    global expression 
    expression = expression + str(num)
    equation.set(expression) 
    
def equalPress():
    try:
        global expression 
        total = str(eval(expression))
        equation.set(total)
        expression = ""
        
    except:
        equation.set("error")
        expression = ""
        
def clear():
    global expression
    expression = ""
    equation.set("")
    
if __name__ == "__main__":
    win = Tk()
    win.configure(background = "grey")
    
    win.title("Python Calculator")
    win.geometry("300x200")
    equation = StringVar()
    
    mainloop()
        