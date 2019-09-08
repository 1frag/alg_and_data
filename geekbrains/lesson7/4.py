# 4. Массив размером 2m + 1, где m – натуральное число,
# заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две
# равные части: в одной находятся элементы, которые не
# меньше медианы, в другой – не больше ее.

# Программа ответ находит тремя путями:
# 1) find вероятностный алгоритм, который при успешных
# randint за линию, а может и вообще никогда не завершиться
# 2) merge_sort - своя сортировка, которая не была представлена
# на уроке
# 3) встроенная функция sort, чтобы проверить ответ


import random
import merge

M = 10
main_lst = [random.randint(-1000, 1000) for _ in range(2 * M + 1)]
print(f'Исходный массив:\n{main_lst}')


def find(mas, k_th):
    if len(set(mas)) == 1:
        return mas[0]
    val = random.choice(mas)
    left, right = [], []
    for elem in mas:
        if elem <= val:
            left.append(elem)
        else:
            right.append(elem)
    if k_th >= len(left):
        return find(right, k_th - len(left))
    else:
        return find(left, k_th)


ans = [0] * 3
ans[0] = find(main_lst, M)
main_lst = merge.merge_sort(main_lst)
print(f'Отсортированный массив:\n{main_lst}')
ans[1] = main_lst[M]
main_lst.sort()
ans[2] = main_lst[M]

for i in range(3):
    print(f'Ответ {i+1}: {ans[i]}')

if len(set(ans)) == 1:
    print('Всё сошлось')
else:
    print('Ой, проблема')
