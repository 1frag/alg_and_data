# 3. В массиве случайных целых чисел поменять
# местами минимальный и максимальный элементы.

import random
SIZE = 10
lst = [random.randint(-500, 500) for _ in range(SIZE)]
ind_min = lst.index(min(lst))
ind_max = lst.index(max(lst))
print(lst)
lst[ind_min], lst[ind_max] = lst[ind_max], lst[ind_min]
print(lst)
