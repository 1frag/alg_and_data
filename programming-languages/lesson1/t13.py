# 3. В первой строке задано количество людей и автомобилей такси,
# в следующих двух строках расстояние в километрах для каждого
# человека и цена за километр для каждого такси. Необходимо
# сопоставить каждому человеку стоимость такси, чтобы суммарная
# цена поездок была минимальна.


def main():
    [n], kms, costs = map(lambda lst: list(map(int, input().split())), '...')
    ord_kms, costs = sorted(range(n), key=lambda x: kms[x]), sorted(costs, reverse=True)
    weight = dict(map(lambda x: x[::-1], enumerate(ord_kms)))
    return '\n'.join(map(lambda x: f'{kms[x]} {costs[weight[x]]}', range(n)))


if __name__ == '__main__':
    print(main())

"""
3
1 2 3
20 10 30

5
3 6 8 9 12
32 42 20 50 31

5
3 6 12 8 9
32 42 20 50 31
"""
