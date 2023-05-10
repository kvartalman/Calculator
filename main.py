from tkinter import *
from re import match

window = Tk()
window.title('Calculator')
window.geometry('200x300')

window.minsize(200, 300)
window.maxsize(200, 300)


def change_sign():
    digit = entry.get()
    if digit:
        if digit[0] == '-':
            digit = digit[1:]
        else:
            digit = '-' + digit
        clear()
        entry.insert(END, digit)


def input_sign(symbol):
    elements = entry.get()
    if len(elements) <= 12:
        if symbol not in '/*+-':
            input_not_operators(symbol)
        elif symbol in '/*+-' and len(elements) > 0 and elements[-1] != '.':
            input_operators(symbol)


def input_operators(symbol):
    elements = entry.get()
    count = 0
    for i in elements:
        if i in '/*+-':
            count += 1
    if count == 0:
        entry.insert(END, symbol)
    elif count == 1:
        if elements.startswith('-') or (symbol == '-' and elements[-1] in '*/+-'):
            entry.insert(END, symbol)
        elif elements[-1].isdigit():
            calculate(symbol)
    elif count == 2:
        if elements.startswith('-') and symbol == '-' and elements[-1] in '*/+-':
            entry.insert(END, symbol)
        elif elements[-1].isdigit():
            calculate(symbol)
    elif count > 2 and elements.count('-') == 2:
        calculate(symbol)


def input_not_operators(symbol):
    elements = entry.get()
    if symbol.isdigit():
        entry.insert(END, symbol)
    elif symbol == '.' and elements[-1] != symbol and len(elements) > 0:
        if elements.count('.') == 0 :
            entry.insert(END, symbol)
        elif elements.count('.') == 1:
            flag = False
            for i in range(1, len(elements)):
                if elements[i] in '-/*+':
                    flag = True
            if flag and elements[-1].isdigit():
                entry.insert(END, symbol)


def clear():
    entry.delete(0, END)


def clear_last():
    elements = entry.get()
    entry.delete(len(elements) - 1)


def calculate(symbol=''):
    elements = entry.get()
    math_signs = '+/-*'
    has_sign = False
    word_checker = False
    for i in elements[1:]:
        if i in math_signs:
            has_sign = True
        if i not in '1234567890/-+*.':
            word_checker = True
    if elements and has_sign and elements[-1].isdigit() and not word_checker:
        clear()
        digits = []
        temp = elements[0]
        sign = ''
        for i in range(1, len(elements)):
            if elements[i].isdigit() or elements[i] == '.':
                temp += elements[i]
            elif elements[i] in '*+/-' and elements[i - 1].isdigit():
                digits.append(float(temp))
                temp = ''
                sign += elements[i]
            elif elements[i] == '-' and elements[i - 1] in '*/-+' and elements[i + 1].isdigit():
                temp += elements[i]
        digits.append(float(temp))

        if sign == '+':
            entry.insert(END, str(calc_sum(digits[0], digits[1])) + symbol)
        elif sign == '-':
            entry.insert(END, str(calc_diff(digits[0], digits[1])) + symbol)
        elif sign == '/':
            entry.insert(END, str(calc_div(digits[0], digits[1])) + symbol)
        else:
            entry.insert(END, str(calc_mult(digits[0], digits[1])) + symbol)


def calc_sum(a, b):
    if a + b == int(a + b):
        return int(a + b)
    return round(a + b, 11)


def calc_diff(a, b):
    if a - b == int(a - b):
        return int(a - b)
    return round(a - b, 11)


def calc_mult(a, b):
    if a * b == int(a * b):
        return int(a * b)
    return round(a * b, 11)


def calc_div(a, b):
    if b == 0:
        return 0
    if a / b == int(a / b):
        return int(a / b)
    return round(a / b, 11)


entry = Entry(window, width=13, font=('', 20), justify=RIGHT)
entry.place(x=0, y=5)


button1 = Button(window, bg='black', fg='yellow', text='1', relief=RIDGE, command=lambda: input_sign('1'))
button1.place(x=0, y=100, width=50, height=50)

button2 = Button(window, bg='black', fg='yellow', text='2', relief=RIDGE, command=lambda: input_sign('2'))
button2.place(x=50, y=100, width=50, height=50)

button3 = Button(window, bg='black', fg='yellow', text='3', relief=RIDGE, command=lambda: input_sign('3'))
button3.place(x=100, y=100, width=50, height=50)

button4 = Button(window, bg='black', fg='yellow', text='4', relief=RIDGE, command=lambda: input_sign('4'))
button4.place(x=0, y=150, width=50, height=50)

button5 = Button(window, bg='black', fg='yellow', text='5', relief=RIDGE, command=lambda: input_sign('5'))
button5.place(x=50, y=150, width=50, height=50)

button6 = Button(window, bg='black', fg='yellow', text='6', relief=RIDGE, command=lambda: input_sign('6'))
button6.place(x=100, y=150, width=50, height=50)


button7 = Button(window, bg='black', fg='yellow', text='7', relief=RIDGE, command=lambda: input_sign('7'))
button7.place(x=0, y=200, width=50, height=50)

button8 = Button(window, bg='black', fg='yellow', text='8', relief=RIDGE, command=lambda: input_sign('8'))
button8.place(x=50, y=200, width=50, height=50)

button9 = Button(window, bg='black', fg='yellow', text='9', relief=RIDGE, command=lambda: input_sign('9'))
button9.place(x=100, y=200, width=50, height=50)

button0 = Button(window, bg='black', fg='yellow', text='0', relief=RIDGE, command=lambda: input_sign('0'))
button0.place(x=0, y=250, width=100, height=50)

button_plus = Button(window, bg='black', fg='yellow', text='+', relief=RIDGE, command=lambda: input_sign('+'))
button_plus.place(x=150, y=200, width=50, height=50)

button_minus = Button(window, bg='black', fg='yellow', text='-', relief=RIDGE, command=lambda: input_sign('-'))
button_minus.place(x=150, y=150, width=50, height=50)

button_div = Button(window, bg='black', fg='yellow', text='/', relief=RIDGE, command=lambda: input_sign('/'))
button_div.place(x=150, y=50, width=50, height=50)

button_mult = Button(window, bg='black', fg='yellow', text='*', relief=RIDGE, command=lambda: input_sign('*'))
button_mult.place(x=150, y=100, width=50, height=50)

button_dot = Button(window, bg='black', fg='yellow', text='.', relief=RIDGE, command=lambda: input_sign('.'))
button_dot.place(x=100, y=250, width=50, height=50)

button_ce = Button(window, bg='black', fg='yellow', relief=RIDGE, text='CE', command=clear)
button_ce.place(x=50, y=50, width=50, height=50)

button_equals = Button(window, bg='black', fg='yellow', relief=RIDGE, text='=', command=calculate)
button_equals.place(x=150, y=250, width=50, height=50)

button_del = Button(window, bg='black', fg='yellow', relief=RIDGE, text='del', command=clear_last)
button_del.place(x=0, y=50, width=50, height=50)

button_plus_minus = Button(window, bg='black', fg='yellow', text='+/-', relief=RIDGE, command=change_sign)
button_plus_minus.place(x=100, y=50, width=50, height=50)


if __name__ == '__main__':
    window.mainloop()
