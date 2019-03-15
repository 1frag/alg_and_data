# 2. Отсортировать по возрастанию методом простого
# выбора одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50). Вывести
# на экран исходный и отсортированный массивы.
import random
import selection


def my_rand(a, b):
    x = random.uniform(a, b)
    while x == b:
        x = random.uniform(a, b)
    return x


N = 5
lst = [my_rand(0, 50) for _ in range(N)]
print(f'Вот что вы ввели:\n{lst}')
selection.selection_sort(lst)
print(f'Оп:\n{lst}')
