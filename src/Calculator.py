from tkinter import *
import math

raice = Tk()
raice.geometry('300x450')
raice.resizable(0,0)
raice.iconbitmap('favicon.ico')
raice.title("PySum")
myFrame = Frame(raice)
myFrame.pack()

operation = ""

def inp(num, equation):
	global operation

	operation = operation + str(num)
	equation.set(operation)
def sq(equation, num):
	global operation

	operation = operation + str(num)
	equation.set(operation)

def Cbutton(equation):
	global operation
	operation = ""
	equation.set("")

def evaluate(equation):
	global operation
	try:
		result = str(eval(operation))
		equation.set(result)
		operation =  ""
	except:
		operation = ""

# ----------------Screen---------------

equation = StringVar()
screen = Entry(myFrame, textvariable = equation)
screen.grid(row=1, column=1, padx=0, pady=18, columnspan=4)
screen.config(background="SystemButtonFace", justify="right", fg="#000000", bd=0, width=18)
screen.configure(font=("Verdana", 18))


# Row 1
def hoverR(e):
	buttonR['bg'] = "gainsboro"	
def leaveR(e):
	buttonR['bg'] = "SystemButtonFace"

buttonC = Button(myFrame, text="C", width=15, height=2, borderwidth=0, bg="gainsboro", command=lambda:Cbutton(equation))
buttonC.grid(row=2, column=1, padx=0, pady=0, columnspan=3)
buttonC.configure(font=("Verdana", 18))
buttonR = Button(myFrame, text="sqrt", width=4, height=2, borderwidth=0, command=lambda:sq(equation, "**0.5"))
buttonR.grid(row=2, column=4, padx=0, pady=0)
buttonR.configure(font=("Verdana", 18))
buttonR.bind("<Enter>", hoverR)
buttonR.bind("<Leave>", leaveR)

# -----------------Row 2--------------------
def hover7(e):
	button7['bg'] = "gainsboro"	
def leave7(e):
	button7['bg'] = "SystemButtonFace"
def hover8(e):
	button8['bg'] = "gainsboro"	
def leave8(e):
	button8['bg'] = "SystemButtonFace"
def hover9(e):
	button9['bg'] = "gainsboro"	
def leave9(e):
	button9['bg'] = "SystemButtonFace"
def hovermult(e):
	multButton['bg'] = "gainsboro"	
def leavemult(e):
	multButton['bg'] = "SystemButtonFace"

button7 = Button(myFrame, text="7", width=4, height=2, borderwidth=0, command=lambda:inp(7, equation))
button7.grid(row=3, column=1, padx=0, pady=0)
button7.configure(font=("Verdana", 18))
button7.bind("<Enter>", hover7)
button7.bind("<Leave>", leave7)
button8 = Button(myFrame, text="8", width=4, height=2, borderwidth=0, command=lambda:inp(8, equation))
button8.grid(row=3, column=2, padx=0, pady=0)
button8.configure(font=("Verdana", 18))
button8.bind("<Enter>", hover8)
button8.bind("<Leave>", leave8)
button9 = Button(myFrame, text="9", width=4, height=2, borderwidth=0, command=lambda:inp(9, equation))
button9.grid(row=3, column=3, padx=0, pady=0)
button9.configure(font=("Verdana", 18))
button9.bind("<Enter>", hover9)
button9.bind("<Leave>", leave9)
multButton = Button(myFrame, text="×", width=4, height=2, borderwidth=0, command=lambda:inp('*', equation))
multButton.grid(row=3, column=4, padx=0, pady=0)
multButton.configure(font=("Verdana", 18))
multButton.bind("<Enter>", hovermult)
multButton.bind("<Leave>", leavemult)

# ---------------Row 3---------------
def hover4(e):
	button4['bg'] = "gainsboro"	
def leave4(e):
	button4['bg'] = "SystemButtonFace"
def hover5(e):
	button5['bg'] = "gainsboro"	
def leave5(e):
	button5['bg'] = "SystemButtonFace"
def hover6(e):
	button6['bg'] = "gainsboro"	
def leave6(e):
	button6['bg'] = "SystemButtonFace"
def hoverdiv(e):
	divButton['bg'] = "gainsboro"	
def leavediv(e):
	divButton['bg'] = "SystemButtonFace"

button4 = Button(myFrame, text="4", width=4, height=2, borderwidth=0, command=lambda:inp(4, equation))
button4.grid(row=4, column=1, padx=0, pady=0)
button4.configure(font=("Verdana", 18))
button4.bind("<Enter>", hover4)
button4.bind("<Leave>", leave4)
button5 = Button(myFrame, text="5", width=4, height=2, borderwidth=0, command=lambda:inp(5, equation))
button5.grid(row=4, column=2, padx=0, pady=0)
button5.configure(font=("Verdana", 18))
button5.bind("<Enter>", hover5)
button5.bind("<Leave>", leave5)
button6 = Button(myFrame, text="6", width=4, height=2, borderwidth=0, command=lambda:inp(6, equation))
button6.grid(row=4, column=3, padx=0, pady=0)
button6.configure(font=("Verdana", 18))
button6.bind("<Enter>", hover6)
button6.bind("<Leave>", leave6)
divButton = Button(myFrame, text="÷", width=4, height=2, borderwidth=0, command=lambda:inp('/', equation))
divButton.grid(row=4, column=4, padx=0, pady=0)
divButton.configure(font=("Verdana", 18))
divButton.bind("<Enter>", hoverdiv)
divButton.bind("<Leave>", leavediv)

# -------------Row 4------------------
def hover1(e):
	button1['bg'] = "gainsboro"	
def leave1(e):
	button1['bg'] = "SystemButtonFace"
def hover2(e):
	button2['bg'] = "gainsboro"	
def leave2(e):
	button2['bg'] = "SystemButtonFace"
def hover3(e):
	button3['bg'] = "gainsboro"	
def leave3(e):
	button3['bg'] = "SystemButtonFace"
def hoverrest(e):
	buttonRest['bg'] = "gainsboro"	
def leaverest(e):
	buttonRest['bg'] = "SystemButtonFace"

button1 = Button(myFrame, text="1", width=4, height=2, borderwidth=0, command=lambda:inp(1, equation))
button1.grid(row=5, column=1, padx=0, pady=0)
button1.configure(font=("Verdana", 18))
button1.bind("<Enter>", hover1)
button1.bind("<Leave>", leave1)
button2 = Button(myFrame, text="2", width=4, height=2, borderwidth=0, command=lambda:inp(2, equation))
button2.grid(row=5, column=2, padx=0, pady=0)
button2.configure(font=("Verdana", 18))
button2.bind("<Enter>", hover2)
button2.bind("<Leave>", leave2)
button3 = Button(myFrame, text="3", width=4, height=2, borderwidth=0, command=lambda:inp(3, equation))
button3.grid(row=5, column=3, padx=0, pady=0)
button3.configure(font=("Verdana", 18))
button3.bind("<Enter>", hover3)
button3.bind("<Leave>", leave3)
buttonRest = Button(myFrame, text="-", width=4, height=2, borderwidth=0,command=lambda:inp('-', equation))
buttonRest.grid(row=5, column=4, padx=0, pady=0)
buttonRest.configure(font=("Verdana", 18))
buttonRest.bind("<Enter>", hoverrest)
buttonRest.bind("<Leave>", leaverest)

# -----------------Row 5------------------
def hover0(e):
	button0['bg'] = "gainsboro"	
def leave0(e):
	button0['bg'] = "SystemButtonFace"
def hoveradd(e):
	addButton['bg'] = "gainsboro"	
def leaveadd(e):
	addButton['bg'] = "SystemButtonFace"
def hovereq(e):
	buttonEq['bg'] = "gainsboro"	
def leaveeq(e):
	buttonEq['bg'] = "SystemButtonFace"
def hoverpoint(e):
	buttonPoint['bg'] = "gainsboro"	
def leavepoint(e):
	buttonPoint['bg'] = "SystemButtonFace"

buttonPoint = Button(myFrame, text=".", width=4, height=2, borderwidth=0, command=lambda:inp('.', equation))
buttonPoint.grid(row=6, column=1, padx=0, pady=0)
buttonPoint.configure(font=("Verdana", 18))
buttonPoint.bind("<Enter>", hoverpoint)
buttonPoint.bind("<Leave>", leavepoint)
button0 = Button(myFrame, text="0", width=4, height=2, borderwidth=0, command=lambda:inp(0, equation))
button0.grid(row=6, column=2, padx=0, pady=0)
button0.configure(font=("Verdana", 18))
button0.bind("<Enter>", hover0)
button0.bind("<Leave>", leave0)
addButton = Button(myFrame, text="+", width=4, height=2, borderwidth=0, command=lambda:inp('+', equation))
addButton.grid(row=6, column=3, padx=0, pady=0)
addButton.configure(font=("Verdana", 18))
addButton.bind("<Enter>", hoveradd)
addButton.bind("<Leave>", leaveadd)
buttonEq = Button(myFrame, text="=", width=4, height=2, borderwidth=0, command=lambda:evaluate(equation))
buttonEq.grid(row=6, column=4, padx=0, pady=0)
buttonEq.configure(font=("Verdana", 18))
buttonEq.bind("<Enter>", hovereq)
buttonEq.bind("<Leave>", leaveeq)

raice.mainloop()
