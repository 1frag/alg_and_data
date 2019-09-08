# 1. Отсортировать по убыванию методом «пузырька»
# одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Вывести на экран
# исходный и отсортированный массивы.
import random
import bubble


def my_rand(a, b):
    x = random.randint(a, b)
    while x == b:
        x = random.randint(a, b)
    return x


N = 5
lst = [my_rand(-100, 100) for _ in range(N)]
print(f'Вот что вы ввели:\n{lst}')
bubble.bubble_sort(lst)
print(f'Оп:\n{lst}')
