# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1D84INGm4IFSnmZ3cOILjh0GNH8VxRwgy/view?usp=sharing

from functools import reduce
n = int(input())
a = list()
while n > 0:
    a.append(n % 10)
    n //= 10
print(reduce(lambda x, y: x*y, a))
print(reduce(lambda x, y: x+y, a))
