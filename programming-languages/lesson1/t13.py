# 3. В первой строке задано количество людей и автомобилей такси,
# в следующих двух строках расстояние в километрах для каждого
# человека и цена за километр для каждого такси. Необходимо
# сопоставить каждому человеку стоимость такси, чтобы суммарная
# цена поездок была минимальна.


def refactor_from_input():
    return list(map(int, input().split()))


def collect_input_data():
    return map(refactor_from_input, range(3))


def get_sorted_lists(n, kms, costs):
    return sorted(range(n), key=lambda x: kms[x]), sorted(costs, reverse=True)


def get_weight(ord_kms):
    return dict(map(lambda x: x[::-1], enumerate(ord_kms)))


def generate_answer(kms, costs, weight, n):
    return '\n'.join(map(lambda x: f'{kms[x]} {costs[weight[x]]}', range(n)))


def main():
    [n], kms, costs = collect_input_data()
    ord_kms, costs = get_sorted_lists(n, kms, costs)
    weight = get_weight(ord_kms)
    return generate_answer(kms, costs, weight, n)


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
