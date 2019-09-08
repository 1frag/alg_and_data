from random import randint as ri

# 1. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого – это цифры числа.

# генерация словарей для дальнейшего использования
dct1 = dict()
for i in range(10):
    dct1[str(i)] = i
for i in range(6):
    dct1[chr(ord('a') + i)] = 10 + i
dct2 = {x: y for y, x in dct1.items()}


# Функция суммирования двух чисел
def sum_16(a, b):
    if len(b) > len(a):
        a, b = b, a
    a.insert(0, '0')
    a = [dct1[x] for x in a][::-1]
    b = [dct1[x] for x in b][::-1]
    for i in range(len(b)):
        a[i] += b[i]
        a[i+1] += a[i] // 16
        a[i] %= 16
    for i in range(len(b), len(a)-1):
        a[i+1] += a[i] // 16
        a[i] %= 16
    while len(a) and a[len(a)-1] == 0:
        a.pop(len(a)-1)
    return [dct2[x] for x in a][::-1]


# умножение на число из одного символа
def small_mul_16(a, b):
    c = ['0']
    for _ in range(b):
        c = sum_16(c, a)
    return c


# возведение в степень (добавление нулей)
def pow_16(a, b):
    for _ in range(b):
        a.append('0')
    return a


# умножение двух чисел
# Умножение делаю в столбик (как учили в школе)
def mul_16(a, b):
    if len(b) > len(a):
        a, b = b, a
    total = ['0']
    b = b[::-1]
    for i in range(len(b)):
        part = small_mul_16(a, dct1[b[i]])
        total = sum_16(total, pow_16(part, i))
    return total


# Функция вывода
def my_print(a):
    res = ''
    for c in a:
        res = res + c
    return res


# Основной код
a, b = map(list, input('Введите 2 числа в 16-ичной СС через пробел:\n').split())
print(f'Сумма этих чисел: {my_print(sum_16(a.copy(), b.copy()))}')
print(f'Произведение чисел: {my_print(mul_16(a.copy(), b.copy()))}')


# Функция для тестирования
def test_mul_16(n):
    for _ in range(n):
        a, b = ri(2, 100000000), ri(2, 100000000)
        c = a * b
        a = list(str(hex(a)))
        b = list(str(hex(b)))
        c = list(str(hex(c)))
        if mul_16(a[2:], b[2:]) != c[2:]:
            print(f'Ошибка при вычислении')
            return
    print('Тесты пройдены успешно')


test_mul_16(100)
