# задача 5, урок 3. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import show_size
SIZE = 10
lst = [random.randint(-10, 10) for _ in range(SIZE)]
print(lst)
try:
    print(max([x for x in lst if x < 0]))
except ValueError:
    print('Да в нем же нет отрицательных элементов!')
else:
    print(show_size.main(list(locals().items())))
