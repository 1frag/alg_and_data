# 3. В первой строке задано количество людей и автомобилей такси,
# в следующих двух строках расстояние в километрах для каждого
# человека и цена за километр для каждого такси. Необходимо
# сопоставить каждому человеку стоимость такси, чтобы суммарная
# цена поездок была минимальна.


def pass_stuff():
    input()


def get_lst():
    return map(int, input().split())


def get_answer():
    return list(
        map(
            lambda x: ' '.join(map(str, sorted(get_lst(), reverse=x))),
            range(2)
        )
    )


if __name__ == '__main__':
    pass_stuff()
    print(*get_answer(), sep='\n')
