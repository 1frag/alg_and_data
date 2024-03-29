# 1. Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа
# не должна завершаться, а должна запрашивать новые данные
# для вычислений. Завершение программы должно выполняться
# при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '*',
# '/'), то программа должна сообщать ему об ошибке и снова
# запрашивать знак операции. Также сообщать пользователю о невозможности
# деления на ноль, если он ввел 0 в качестве делителя.

# https://drive.google.com/file/d/11srjKp5dDhRr-GnD6Z5kSW2ihFGn41b4/view?usp=sharing


def f(a, b, sign):
    if sign == '+':
        return a + b
    if sign == '-':
        return a - b
    if sign == '*':
        return a * b
    return a / b


do = '#'
sign = {'+', '-', '*', '/', '0'}

while True:
    do = input('Введите знак опрации: ')
    while not(do in sign):
        do = input('Введите корректный знак: ')
    if do == '0':
        break
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    while b == '0' and do == '/':
        print('Вы не имеете права делить на ноль')
        b = input('Измените второе число: ')
    # использование возможностей python'a
    # print('Результат {}'.format(eval(a+do+b)))
    # без использования
    print('Результат {}'.format(f(int(a), int(b), do)))
print('Спасибо, с вами было приятно работать')
