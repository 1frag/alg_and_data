# Задача: на вход подается 2 натуральных числа a и b
# требуется посчитать a ** b
import math
import random


def pow1(a, b):
    return a ** b


def pow2(a, b):
    res = 1
    for _ in range(b):
        res *= a
    return res


def pow3(a, b):
    if b == 0:
        return 1
    if b % 2:
        return a * pow3(a, b-1)
    else:
        c = pow3(a, b//2)
        return c * c


def pow4(a, b):
    res = 1
    while b:
        if b % 2:
            res *= a
            b -= 1
        else:
            a *= a
            b //= 2
    return res


def test(n):
    for _ in range(n):
        result = [0 for _ in range(4)]
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        for i in range(1, 5):
            dct = {1: pow1, 2: pow2, 3: pow3, 4: pow4}
            result[i-1] = dct[i](a, b)
        if len(set(result)) != 1:
            print(f'Ошибка при вычислении {a} ** {b}:')
            for i in range(1, 5):
                print(f'{i}) {result[i-1]}')


# test(200)

# python -m timeit -n 100 -s "import bonus" "bonus.pow4(13, 10000)"

# пусть A = 13, B = 10000

# "bonus.pow1(13, 10000)"
# 100 loops, best of 3: 724 usec per loop

# "bonus.pow2(13, 10000)"
# 100 loops, best of 3: 16.4 msec per loop

# "bonus.pow3(13, 10000)"
# 100 loops, best of 3: 929 usec per loop

# "bonus.pow4(13, 10000)"
# 100 loops, best of 3: 1.29 msec per loop

# 1 реализация с помощью стандартной функции python
# 2 реализация в цикле втупую умножаем столько раз, сколько надо
# 3 реализация рекурсивное бинарное возведение в степень
# 4 реализация рекурентое бинарное возведение в степень

# Как и ожидалось 2 реализация никуда не годится и потратила больше всего времени
# Два последних алгоритма имеют логарифмическую сложность
# однако рекурсивная реализация оказалась быстрее (ожидал наоборот)
# А в итоге выиграла pow1, которая и пишется быстрее всех и работает
