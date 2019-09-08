from collections import defaultdict as d_dict

# Обрабатываем пользовательский ввод
inp = input('Введите что кодировать:\n')
dct = d_dict(int)
for c in inp:
    dct[c] += 1


class Node:

    def __init__(self, data=None, left=None, right=None):
        # Инициализация:
        # либо вершина имеет данные - значит она лист
        # либо данных не имеет, а имеет левого и правого сына
        self.left = left
        self.right = right
        if data is None:
            data = tuple([None, left.get_value()+right.get_value()])
        self.data = data

    def get_value(self):
        return self.data[1]


def dfs(elem, path):
    # Стандартный обход дерева:
    # добрались до листа - присвоили символу код
    if elem.left is None:
        code[elem.data[0]] = path
        return
    dfs(elem.left, path + '0')
    dfs(elem.right, path + '1')


# Я пользуюсь двумя массивами. Изначально второй пустой
# в конец второго добавляю вновь-образованные Nodы
# такое добавление не ломает отсортированность массивов
# а значит вновь-образованные Node может получиться из:
# двух первых элементов в первом массиве
# двух первых элементов из второго массива
# первый элемент из первого и второго массива
# Чтобы не тратить время на удаление первого элемента из списка
# двигаю идексы i, j для data1 и data2 соответственно
# Подробнее об алгоритме на neerc.ifmo.ru/wiki/index.php?title=Алгоритм_Хаффмана_за_O(n)
data1 = [Node(tuple([x[0], x[1]])) for x in dct.items()]
data1.sort(key=lambda x: x.get_value())
data2 = list()
i, j = 0, 0
while len(data1) + len(data2) > 1 + i + j:
    new_elem = [None] * 3
    if len(data1) > i + 1:
        new_elem[0] = Node(left=data1[i], right=data1[i+1])
    if len(data2) > j + 1:
        new_elem[1] = Node(left=data2[j], right=data2[j+1])
    if len(data1) > i and len(data2) > j:
        new_elem[2] = Node(left=data1[i], right=data2[j])
    min_val = min([x.get_value() for x in new_elem if x is not None])
    for k in range(3):
        if new_elem[k] is not None and new_elem[k].get_value() == min_val:
            if k == 0:
                i += 2
            if k == 1:
                j += 2
            if k == 2:
                i, j = i+1, j+1
            data2.append(new_elem[k])
            break


# В итоге остался лишь 1 элемент data2[j]
# в нём лежит настоящее дерево по этому
# дереву мы и запускаем дфс

code = dict()
dfs(data2[j], '')
print(f'Вот ваша строка: {inp}')
print('Каждый символ заменён на код')
print('Вот коды символов:')
for key, val in code.items():
    print(f"'{key}' - {val}")
print('Вот что получилось в итоге:')
for c in inp:
    print(code[c], end=' ')
