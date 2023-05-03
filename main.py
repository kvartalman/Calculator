from tkinter import *

window = Tk()
window.title('Calculator')
window.geometry('200x300')

window.minsize(200, 300)
window.maxsize(200, 300)


def change_sign():                   # Меняем знак числа
    digit = entry.get()
    if digit:                        # Делаем только если не в поле ввода что-то было
        if digit[0] == '-':
            digit = digit[1:]
        else:
            digit = '-' + digit
        clear()
        entry.insert(END, digit)


def input_digit(symbol):
    elements = entry.get()
    if len(elements) <= 13:                              # Поле ввода ограничено 13-ю символами
        if symbol not in '/*+-':
            entry.insert(END, symbol)
        else:                                            # Если попалось математическое действие, то проверяем, было ли
            count = 0                                    # ранее введено мат. действие, если было - сперва выполняем
            for j in elements:                           # расчёт, выводим в поле ввода и добавляем знак мат. действия
                if not j.isdigit() and j != '.':
                    count += 1
            if count > 0:
                calculate(symbol)
            else:
                entry.insert(END, symbol)


def clear():                         # Очистка поля ввода
    entry.delete(0, END)


def clear_last():                    # Удаление последнего элемента поля ввода
    elements = entry.get()
    entry.delete(len(elements) - 1)


def calculate():                 # Вызывается при нажатии знака "равно" или использовании
    elements = entry.get()       # -1231241/1231231
    math_signs = '+/-*'
    has_sign = False
    for i in elements[1:]:
        if i in math_signs:
            has_sign = True
            break
    if elements and has_sign:
        clear()
        digits = []
        temp = elements[0]
        sign = ''
        for i in range(1, len(elements)):
            if elements[i].isdigit():
                temp += elements[i]
            elif elements[i] in '*+/-' and elements[i - 1].isdigit():
                digits.append(int(temp))           # если calculate вызывается со знаком равно - просто считаем, а если с
                temp = ''                          # другим знаком - этот знак добавим в конце выражения
                sign += elements[i]
            elif elements[i] == '-' and elements[i - 1] in '*/-+' and elements[i + 1].isdigit():
                temp += elements[i]
        digits.append(int(temp))

        if sign == '+':
            entry.insert(END, calc_sum(digits[0], digits[1]))
        elif sign == '-':
            entry.insert(END, calc_diff(digits[0], digits[1]))
        elif sign == '/':
            entry.insert(END, calc_div(digits[0], digits[1]))
        else:
            entry.insert(END, calc_mult(digits[0], digits[1]))


def calc_sum(a, b):
    return a + b


def calc_diff(a, b):
    return a - b


def calc_mult(a, b):
    return a * b


def calc_div(a, b):
    return a / b


entry = Entry(window, width=13, font=('', 20))
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
