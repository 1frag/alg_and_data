import sys


def show_iter_size(elem):
    # Какие значения считаются в общей сумме:
    # print(elem)
    res = sys.getsizeof(elem)
    if hasattr(elem, '__iter__'):
        if hasattr(elem, 'items'):
            for x in elem.items():
                res += show_iter_size(x)
        elif not isinstance(elem, str):
            for x in elem:
                res += show_iter_size(x)
    return res


def main(all_variables):
    sum_ = 0
    for key, val in all_variables:
        if key.startswith('__'):
            continue
        if str(val.__class__).endswith("'module'>"):
            continue
        if str(val.__class__).endswith("'function'>"):
            continue
        sum_ += show_iter_size(val)
    return f'Затраченное количество памяти: {sum_}'


if __name__ == '__main__':
    # Пример работы:
    my_int_1 = 5
    my_int_2 = 200000000000000
    my_str_1 = 'qwe'
    my_str_2 = 'qqqqqqqqqqqqqqqqqqqqqqqqqqqq'
    my_list = ['1', 'b', 3, 'IV', (5, 6, 7)]
    my_dict = {'main': main, 'show_iter_size': show_iter_size}
    my_set = {i for i in range(10)}
    print(main(list(locals().items())))
