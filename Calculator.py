from tkinter import*
import tkinter as tk
def click(num):
    value = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, value + str(num))
def clear():
    entry.delete(0, tk.END)
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def click_1():
    click(1)
def click_2():
    click(2)
def click_3():
    click(3)
def click_4():
    click(4)
def click_5():
    click(5)
def click_6():
    click(6)
def click_7():
    click(7)
def click_8():
    click(8)
def click_9():
    click(9)
def click_0():
    click(0)
def click_add():
    click("+")
def click_subtract():
    click("-")
def click_multiply():
    click("*")
def click_divide():
    click("/")
window = Tk()
window.title("CALCULATOR")
window.geometry("400x300+150+150")
entry = Entry(window, width=35)
entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
button1 = Button(window, text="1", width=10, height=3, command=click_1)
button2 = Button(window, text="2", width=10, height=3, command=click_2)
button3 = Button(window, text="3", width=10, height=3, command=click_3)
button4 = Button(window, text="4", width=10, height=3, command=click_4)
button5 = Button(window, text="5", width=10, height=3, command=click_5)
button6 = Button(window, text="6", width=10, height=3, command=click_6)
button7 = Button(window, text="7", width=10, height=3, command=click_7)
button8 = Button(window, text="8", width=10, height=3, command=click_8)
button9 = Button(window, text="9", width=10, height=3, command=click_9)
button0 = Button(window, text="0", width=10, height=3, command=click_0)
add = Button(window, text="+", width=10, height=3, command=click_add)
subtract = Button(window, text="-", width=10, height=3, command=click_subtract)
multiply = Button(window, text="*", width=10, height=3, command=click_multiply)
divide = Button(window, text="/", width=10, height=3, command=click_divide)
bnequal = Button(window, text="=", width=15, height=3, command=equal)
bnclear = Button(window, text="Clear", width=15, height=3, command=clear)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
bnclear.grid(row=4, column=1)
add.grid(row=3, column=3)
bnequal.grid(row=4, column=2)
subtract.grid(row=2, column=3)
multiply.grid(row=1, column=3)
divide.grid(row=4, column=3)
window.mainloop()
