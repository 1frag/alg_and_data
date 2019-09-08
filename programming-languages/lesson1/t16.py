# 6. Напишите программу для масштабирования треугольников. Входные
# данные: количество треугольников, список координат вершин в формате
# xA yA xB yB xC yC, коэффициент масштабирования. Выходные данные:
# список масштабированных векторов, задающих стороны треугольника.
"""
Хардкодить массив:
[(2, 0), (3, 1), (4, 2), (5, 3), (0, 4), (1, 5)]
не очень приятно, но генерировать его еще хуже:
from functools import reduce
zip(*[map(
    lambda x: x[1] + (x[0] // 2) % 2,
    enumerate(reduce(
        lambda x, y: x + y,
        map(lambda x: [(x + 2) % 6, x] * 2, [0, 2, 4])
    ))
)] * 2)
"""


def get_indexes():
    return [(2, 0), (3, 1), (4, 2), (5, 3), (0, 4), (1, 5)]


def collect(num):
    triangle = lambda: list(map(int, input().split()))
    return (num and collect(num - 1) + [triangle()]) or [triangle()]


def output(row, scale=None):
    return ' '.join(map(
        lambda x: str(scale * (row[x[0]] - row[x[1]])),
        get_indexes()
    ))


def main():
    data = collect(int(input()) - 1)
    output.__defaults__ = (int(input()), )
    return '\n'.join(map(output, data))


if __name__ == '__main__':
    print(main())

"""
3
7 0 0 4 7 4
7 0 3 0 7 3
6 0 3 0 3 4
2

-14 8 14 0 0 -8
-8 0 8 6 0 -6
-6 0 0 8 6 -8

"""
