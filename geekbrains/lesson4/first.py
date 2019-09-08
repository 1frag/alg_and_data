# 1. Проанализировать скорость и сложность одного любого
#  алгоритма, разработанных в рамках домашнего задания
# первых трех уроков.

import cProfile
import random
import timeit


def main(size):
    lst1 = [random.randint(0, 1000) for _ in range(int(size))]
    lst2 = [i for i, x in enumerate(lst1) if x % 2 == 0]
    return lst2


# cProfile.run("main(10000)")

# python -m timeit -n 100 -s "import first" "first.main( 100000 )"

# "first.main(100)"
# 100 loops, best of 3: 173 usec per loop

# "first.main( 1000 )"
# 100 loops, best of 3: 1.69 msec per loop
