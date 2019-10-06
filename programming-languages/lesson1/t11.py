# 1. Напишите программу, которая считывает количество элементов
# массив и массив из потока ввода и вычисляет сумму всех его
# элементов и выводит результат на экран.


def eval_sum(lst):
    return sum(map(int, lst.split()))


def get_lst():
    return (input(), input())[1]


if __name__ == '__main__':
    print(eval_sum(get_lst()))
