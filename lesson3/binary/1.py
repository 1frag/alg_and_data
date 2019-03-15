# Дан отсортированный массив на n элементов.
# Определить количество чисел строго больших чем x.
# формат ввода:
# n x
# a1 a2 ... an

n, x = map(int, input().split())
a = list(map(int, input().split()))
left, right, last_suc = 0, n-1, n
while left <= right:
    mid = (left + right) // 2
    if a[mid] <= x:
        left = mid + 1
    else:
        last_suc = mid
        right = mid - 1
print(n-last_suc)

# Примеры:
# >>>5 3
# >>>1 2 3 4 5
# 2
# >>>5 6
# >>>1 2 3 4 5
# 0
# >>>5 0
# >>>1 2 3 4 5
# 5

# В данной задаче мы находим бинарным поиском
# индекс первого элемента, который больше x
