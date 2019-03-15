# 9. Найти максимальный элемент среди минимальных
# элементов столбцов матрицы.

import random
INF = 99  # наибольшее которое может быть сгенерировано
SIZE = 10
matrix = [[random.randint(0, INF) for _ in range(SIZE)] for _ in range(SIZE)]
print('Сгенерирована матрица:')
for line in matrix:
    for elem in line:
        print(elem, end=' ')
    print('')
min_val = [INF] * SIZE
for i in range(SIZE):
    for j in range(SIZE):
        min_val[j] = min(min_val[j], matrix[i][j])
print('А вот и ответ: {}'.format(max(min_val)))
