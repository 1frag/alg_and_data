# 2. Напишите функцию, которая выводит все нечётные цифры числа n.
# Используя эту функцию, напишите программу, которая считывает
# число n из потока ввода и выводит все его нечётные цифры.
# Использование массивов и строк в этой задаче запрещено.


def get_number_from_input():
    return int(input())


def fun(num, res=0):
    res = (num > 9) and fun(num // 10)
    res = ((num % 2) and (res * 10 + num % 10)) or res
    return int(res)


if __name__ == '__main__':
    print(fun(get_number_from_input()))
