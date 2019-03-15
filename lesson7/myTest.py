import random


def check(func, reverse = False):
    N = 100
    M = 100
    for i in range(M):
        lst1 = [random.randint(-100, 100) for _ in range(N)]
        lst2 = lst1.copy()
        func(lst1)
        lst2.sort()
        if reverse:
            lst2.reverse()
        if lst1 != lst2:
            return 'Проверка не пройдена'
    return 'Проверка пройдена успешно'
