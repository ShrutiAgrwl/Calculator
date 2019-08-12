import math
import tkinter as t

winC = t.Tk()


def btnclick(n):
    global operators
    operators = operators + str(n)
    txt_input.set(operators)


def replace():
    global operators
    val = str(math.pi)
    operators = operators.replace('pi', val)
    operators = operators.replace('x', '*')
    operators = operators.replace('^', '**')


def btnclearall():
    global operators
    operators = ""
    txt_input.set("")


def btnclr():
    global operators
    operators = operators[:-1]
    if operators:
        txt_input.set(operators)
    else:
        txt_input.set(0)


def btnequals():
    global operators
    replace()
    try:
        equal = str(eval(operators))
        txt_input.set(equal)
        operators = equal
    except:
        operators = ''
        txt_input.set('error')


def sign():
    global operators
    try:
        o = operators
        op = o.find('.')
        if op == -1:
            o = -(int(o))
        else:
            o = -(float(o))
        operators = str(o)
        txt_input.set(operators)
    except:
        operators = ''
        txt_input.set('error')


def calsqrt():
    global operators
    try:
        op = float(txt_input.get())
        operators = str(math.sqrt(op))
        txt_input.set(operators)
        operators = ''
    except:
        operators = ''
        txt_input.set('error')


def factno():
    global operators
    try:
        op = int(operators)
        fact = 1
        for i in range(1, (op + 1)):
            fact = fact * i
        txt_input.set(str(fact))
        operators = str(fact)
    except:
        operators = ''
        txt_input.set('error')


def div():
    global operators
    try:
        o = operators
        o = 1 / float(o)
        operators = str(o)
        txt_input.set(operators)
        operators = ''
    except:
        operators = ''
        txt_input.set('error')


winC.title('Calculator')
winC.geometry('385x380')
txt = ('arial', 22, 'bold')
txt1 = ('arial', 10, 'bold')
winC.resizable(0,0)
operators = ""
txt_input = t.StringVar()

e = t.Entry(winC, font=txt, bd=30, justify='right', textvariable=txt_input,
            bg='lightgrey').grid(row=1, columnspan=8)

bac = t.Button(winC, text='AC', width=14, height=2, fg='white', bg='black',
               font=txt1, bd=4, command=lambda: btnclearall()).grid(row=2, columnspan=2)
bclr = t.Button(winC, text='C', width=14, height=2, fg='white', bg='black',
                font=txt1, bd=4, command=lambda: btnclr()).grid(row=2, column=2, columnspan=2)
bcls = t.Button(winC, text='Close', width=14, height=2, fg='white', bg='black',
                font=txt1, bd=4, command=lambda: quit()).grid(row=2, column=4, columnspan=2)

b7 = t.Button(winC, text='7', width=6, height=2, fg='white', bg='black',
              font=txt1, bd=4, command=lambda: btnclick(7)).grid(row=3, column=0)
b8 = t.Button(winC, text='8', width=6, height=2, fg='white', bg='black',
              font=txt1, bd=4, command=lambda: btnclick(8)).grid(row=3, column=1)
b9 = t.Button(winC, text='9', width=6, height=2, fg='white', bg='black',
              font=txt1, bd=4, command=lambda: btnclick(9)).grid(row=3, column=2)
badd = t.Button(winC, text='+', width=6, height=2, fg='white', bg='black',
                font=txt1, bd=4, command=lambda: btnclick('+')).grid(row=3, column=3)
bfact = t.Button(winC, text='x!', width=6, height=2, fg='white', bg='black',
                 font=txt1, bd=4, command=lambda: factno()).grid(row=3, column=4)
bmod = t.Button(winC, text='%', width=6, height=2, fg='white', bg='black',
                font=txt1, bd=4, command=lambda: btnclick('%')).grid(row=3, column=5)

b4 = t.Button(winC, text='4', width=6, height=2, fg='white', bg='black',
              font=txt1, bd=4, command=lambda: btnclick(4)).grid(row=4, column=0)
b5 = t.Button(winC, text='5', width=6, height=2, fg='white', bg='black',
              font=txt1, bd=4, command=lambda: btnclick(5)).grid(row=4, column=1)
b6 = t.Button(winC, text='6', width=6, height=2, fg='white', bg='black',
              font=txt1, bd=4, command=lambda: btnclick(6)).grid(row=4, column=2)
bsub = t.Button(winC, text='-', width=6, height=2, fg='white', bg='black',
                font=txt1, bd=4, command=lambda: btnclick('-')).grid(row=4, column=3)
b11 = t.Button(winC, text='(', width=6, height=2, fg='white', bg='black',
               font=txt1, bd=4, command=lambda: btnclick('(')).grid(row=4, column=4)
b12 = t.Button(winC, text=')', width=6, height=2, fg='white', bg='black',
               font=txt1, bd=4, command=lambda: btnclick(')')).grid(row=4, column=5)

b1 = t.Button(winC, text='1', width=6, height=2, fg='white', bg='black',
              font=txt1, bd=4, command=lambda: btnclick(1)).grid(row=5, column=0)
b2 = t.Button(winC, text='2', width=6, height=2, fg='white', bg='black',
              font=txt1, bd=4, command=lambda: btnclick(2)).grid(row=5, column=1)
b3 = t.Button(winC, text='3', width=6, height=2, fg='white', bg='black',
              font=txt1, bd=4, command=lambda: btnclick(3)).grid(row=5, column=2)
bmult = t.Button(winC, text='x', width=6, height=2, fg='white', bg='black',
                 font=txt1, bd=4, command=lambda: btnclick('x')).grid(row=5, column=3)
bsq = t.Button(winC, text='sqrt', width=6, height=2, fg='white', bg='black',
               font=txt1, bd=4, command=lambda: calsqrt()).grid(row=5, column=4)
bpow = t.Button(winC, text='^', width=6, height=2, fg='white', bg='black',
                font=txt1, bd=4, command=lambda: btnclick('^')).grid(row=5, column=5)

b10 = t.Button(winC, text='0', width=6, height=2, fg='white', bg='black',
               font=txt1, bd=4, command=lambda: btnclick(0)).grid(row=6, column=0)
b13 = t.Button(winC, text='.', width=6, height=2, fg='white', bg='black',
               font=txt1, bd=4, command=lambda: btnclick('.')).grid(row=6, column=1)
b14 = t.Button(winC, text='+/-', width=6, height=2, fg='white', bg='black',
               font=txt1, bd=4, command=lambda: sign()).grid(row=6, column=2)
b15 = t.Button(winC, text='/', width=6, height=2, fg='white', bg='black',
               font=txt1, bd=4, command=lambda: btnclick('/')).grid(row=6, column=3)
bpi = t.Button(winC, text='pi', width=6, height=2, fg='white', bg='black',
               font=txt1, bd=4, command=lambda: btnclick('pi')).grid(row=6, column=4)
b17 = t.Button(winC, text='1/x', width=6, height=2, fg='white', bg='black',
               font=txt1, bd=4, command=lambda: div()).grid(row=6, column=5)

b16 = t.Button(winC, text='=', width=31, height=1, fg='white', bg='black',
               font=('arial', 15, 'bold'), bd=4, command=lambda: btnequals()).grid(row=7, columnspan=6)

winC.config(bg='darkblue')
winC.mainloop()
