import tkinter as tk
import math


root = tk.Tk()
root.title('Calculator')
root.iconbitmap('icon.ico')

e = tk.Entry(root, width=65)
e.grid(row=0, column=0, columnspan=5, padx=10,pady=10)

num_x = 0
numstr = 0

def number(x):
	zm = e.get()+str(x)
	e.delete(0, tk.END)
	e.insert(0, zm)
	
def equ():
	global num_x
	global numstr
	num_x = e.get()
	e.delete(0, tk.END)
	wyn = eval(numstr+num_x)
	e.insert(0, wyn)
	num_x = 0
	
def add():
	global numstr
	global num_x
	num_x = e.get()
	e.delete(0, tk.END)
	numstr = str(num_x)+'+'
	num_x = 0

def minus():
	global numstr
	global num_x
	num_x = e.get()
	e.delete(0, tk.END)
	numstr = str(num_x)+'-'
	num_x = 0
	
def multip():
	global numstr
	global num_x
	num_x = e.get()
	e.delete(0, tk.END)
	numstr = str(num_x)+'*'
	num_x = 0

def divided():
	global numstr
	global num_x
	num_x = e.get()
	e.delete(0, tk.END)
	numstr = str(num_x)+'/'
	num_x = 0

def square():
	global numstr
	global num_x
	num_x = int(e.get())
	numstr = str(math.sqrt(num_x))
	e.insert(0, numstr)
	num_x = 0
	numstr = ''

def pow():
	global numstr
	global num_x
	num_x = e.get()
	e.delete(0, tk.END)
	numstr = str(num_x)+'**'
	num_x = 0

def clear():
	global numstr
	global num_x
	numstr = ''
	num_x = 0
	e.delete(0, tk.END)
	

Btn_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: number(1))
Btn_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: number(2))
Btn_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: number(3))
Btn_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: number(4))
Btn_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: number(5))
Btn_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: number(6))
Btn_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: number(7))
Btn_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: number(8))
Btn_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: number(9))
Btn_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: number(0))
Btn_multi = tk.Button(root, text="x", padx=40, pady=20, command=multip)
Btn_add = tk.Button(root, text="+", padx=40, pady=20, command=add)
Btn_minus = tk.Button(root, text="-", padx=40, pady=20, command=minus)
Btn_divided = tk.Button(root, text="/", padx=40, pady=20, command=divided)
Btn_square = tk.Button(root, text="/**", padx=40, pady=20, command=square)
Btn_pow = tk.Button(root, text="x^x", padx=40, pady=20, command=pow)
Btn_equ = tk.Button(root, text="=", padx=40, pady=20, command=equ)
Btn_clear = tk.Button(root, text="clear", padx=40, pady=20, command=clear)

Btn_1.grid(row=1, column=0, sticky='WE')
Btn_2.grid(row=1, column=1, sticky='WE')
Btn_3.grid(row=1, column=2, sticky='WE')
Btn_4.grid(row=2, column=0, sticky='WE')
Btn_5.grid(row=2, column=1, sticky='WE')
Btn_6.grid(row=2, column=2, sticky='WE')
Btn_7.grid(row=3, column=0, sticky='WE')
Btn_8.grid(row=3, column=1, sticky='WE')
Btn_9.grid(row=3, column=2, sticky='WE')
Btn_0.grid(row=4, column=0, sticky='WE')
Btn_multi.grid(row=1, column=4, sticky='WE')
Btn_add.grid(row=2, column=4, sticky='WE')
Btn_minus.grid(row=3, column=4, sticky='WE')
Btn_divided.grid(row=4, column=4, sticky='WE')
Btn_pow.grid(row=4, column=1, sticky='WE')
Btn_square.grid(row=4, column=2, sticky='WE')
Btn_equ.grid(row=5, column=0, columnspan=3, sticky='WE')
Btn_clear.grid(row=5, column=4, sticky='WE')


root.mainloop()