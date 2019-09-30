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


def make_triangle_from_input():
    return list(map(int, input().split()))


def collect(num):
    _ = make_triangle_from_input
    return (num and collect(num - 1) + [_()]) or [_()]


def make_scaling(x, scale, row):
    return str(scale * (row[x[0]] - row[x[1]]))


def output(row, scale):
    return ' '.join(map(
        lambda x: make_scaling(x, scale, row),
        get_indexes()
    ))


def put_default_scale(scale):
    output.__defaults__ = (scale, )


def get_scale():
    return int(input())


def get_count():
    return int(input()) - 1


def get_total_data(pre_data):
    return '\n'.join(map(output, pre_data))


def main():
    data = collect(get_count())
    put_default_scale(get_scale())
    return get_total_data(data)


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
