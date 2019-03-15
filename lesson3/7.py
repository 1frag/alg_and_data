# 7. В одномерном массиве целых чисел определить два
# наименьших элемента. Они могут быть как равны между
# собой (оба являться минимальными), так и различаться.

import random
SIZE = 10  # >1
lst = [random.randint(0, 10) for _ in range(SIZE)]
print(lst)
# решение 1: за линию


def swap_if(a, b):
    if a > b:
        return b, a
    else:
        return a, b


min1, min2 = [max(lst)] * 2
for elem in lst:
    min2, elem = swap_if(min2, elem)
    min1, min2 = swap_if(min1, min2)
print(min1, min2)

# решение 2: O(N*logN), но короче:
lst.sort()
print(*lst[:2])
