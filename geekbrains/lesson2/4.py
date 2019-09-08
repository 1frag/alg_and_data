# 4. Найти сумму n элементов следующего ряда
# чисел: 1 -0.5 0.25 -0.125 ...Количество
# элементов (n) вводится с клавиатуры.

n = int(input('Введите количество чисел ряда: '))

# по формуле для геометрической прогрессии (b_1 = 1, q = -0.5):
b_n = (-0.5) ** (n - 1)
s_n = (b_n + 2) / 3

# циклом:
# https://drive.google.com/file/d/1x9xPy7L26lD62gD4kLnHDDhw-b7x_fkF/view?usp=sharing
# наверно решение формулой не нуждается в блок схеме?
sum, a = 0, 1
while n:
    n -= 1
    sum += a
    a /= -2
print('Ответ формулой {}'.format(s_n))
print('Ответ циклом {}'.format(sum))