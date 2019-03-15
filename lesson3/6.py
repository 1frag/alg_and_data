# 6. В одномерном массиве найти сумму элементов, находящихся
# между минимальным и максимальным элементами. Сами минимальный
# и максимальный элементы в сумму не включать.

import random
SIZE = 10
lst = [random.randint(-500, 500) for _ in range(SIZE)]
i = lst.index(min(lst))
j = lst.index(max(lst))
if i > j:
    i, j = j, i
print(lst)
print(sum([lst[k] for k in range(i+1, j)]))
