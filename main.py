from tkinter import *

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


def input_digit(symbol):
    elements = entry.get()
    if len(elements) <= 12:
        if symbol not in '/*+-':
            entry.insert(END, symbol)
        elif symbol in '/*+-' and len(elements) > 0:
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

button1 = Button(window, bg='black', fg='yellow', text='1', command=lambda: input_digit('1'))
button1.place(x=0, y=100, width=50, height=50)

button2 = Button(window, bg='black', fg='yellow', text='2', command=lambda: input_digit('2'))
button2.place(x=50, y=100, width=50, height=50)

button3 = Button(window, bg='black', fg='yellow', text='3', command=lambda: input_digit('3'))
button3.place(x=100, y=100, width=50, height=50)

button4 = Button(window, bg='black', fg='yellow', text='4', command=lambda: input_digit('4'))
button4.place(x=0, y=150, width=50, height=50)

button5 = Button(window, bg='black', fg='yellow', text='5', command=lambda: input_digit('5'))
button5.place(x=50, y=150, width=50, height=50)

button6 = Button(window, bg='black', fg='yellow', text='6', command=lambda: input_digit('6'))
button6.place(x=100, y=150, width=50, height=50)

button7 = Button(window, bg='black', fg='yellow', text='7', command=lambda: input_digit('7'))
button7.place(x=0, y=200, width=50, height=50)

button8 = Button(window, bg='black', fg='yellow', text='8', command=lambda: input_digit('8'))
button8.place(x=50, y=200, width=50, height=50)

button9 = Button(window, bg='black', fg='yellow', text='9', command=lambda: input_digit('9'))
button9.place(x=100, y=200, width=50, height=50)

button0 = Button(window, bg='black', fg='yellow', text='0', command=lambda: input_digit('0'))
button0.place(x=0, y=250, width=100, height=50)

button_plus = Button(window, bg='black', fg='yellow', text='+', command=lambda: input_digit('+'))
button_plus.place(x=150, y=200, width=50, height=50)

button_minus = Button(window, bg='black', fg='yellow', text='-', command=lambda: input_digit('-'))
button_minus.place(x=150, y=150, width=50, height=50)

button_div = Button(window, bg='black', fg='yellow', text='/', command=lambda: input_digit('/'))
button_div.place(x=150, y=50, width=50, height=50)

button_mult = Button(window, bg='black', fg='yellow', text='*', command=lambda: input_digit('*'))
button_mult.place(x=150, y=100, width=50, height=50)

button_dot = Button(window, bg='black', fg='yellow', text='.', command=lambda: input_digit('.'))
button_dot.place(x=100, y=250, width=50, height=50)

button_ce = Button(window, bg='black', fg='yellow', text='CE', command=clear)
button_ce.place(x=50, y=50, width=50, height=50)

button_equals = Button(window, bg='black', fg='yellow', text='=', command=calculate)
button_equals.place(x=150, y=250, width=50, height=50)

button_del = Button(window, bg='black', fg='yellow', text='del', command=clear_last)
button_del.place(x=0, y=50, width=50, height=50)

button_plus_minus = Button(window, bg='black', fg='yellow', text='+/-', command=change_sign)
button_plus_minus.place(x=100, y=50, width=50, height=50)


if __name__ == '__main__':
    window.mainloop()
