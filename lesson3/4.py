# 4. Определить, какое число в массиве встречается чаще всего.
import random
SIZE = 100
lst = [random.randint(1, 5) for _ in range(SIZE)]
# print(lst)
# решение в одну строку, но за О(N**2)
print(max(lst, key=lst.count))
# другое решение
dct = {x: 0 for x in set(lst)}
for x in lst:
    dct[x] += 1
print(max(dct.keys(), key=dct.get))

# Иногда ответы получаются разные, потому что максимальное
# число раз встречаются несколько чисел
