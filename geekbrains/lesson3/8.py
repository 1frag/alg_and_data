# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних
# элементов строк. Программа должна вычислять сумму введенных
# элементов каждой строки и записывать ее в ее последнюю
# ячейку. В конце следует вывести полученную матрицу.

matrix = [[0 for _ in range(5)] for _ in range(4)]
print('Вводите первые 4 числа каждой из 4 строк в формате: x y z w')
for i in range(4):
    matrix[i][:4] = map(int, input().split())
    matrix[i][4] = sum(matrix[i][:4])
print('Итоговая матрица:')
for line in matrix:
    for elem in line:
        print(elem, end=' ')
    print('')

# Пример ввода:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
