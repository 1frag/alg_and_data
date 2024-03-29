# Решить уравнение f(x)=A, f(x)= (x**3) + 2*(x**2) + 3*x + 4
# На ввод подается значение A, гарантируется f(-100)<=A<=f(100)


def f(x):
    return (x**3) + 2*(x**2) + 3*x + 4


A = int(input())
P = 100  # Точность вычисления
left, right = -100, 100
for _ in range(P):
    mid = (left + right) / 2
    if f(mid) > A:
        right = mid
    elif f(mid) < A:
        left = mid
    else:
        break
print((left + right) / 2)

# Примеры:
# >>>10
# 1.0
# >>>194
# 5.0
# >>>777
# 8.455947660100332

# В данной задаче можно применить бинарный поиск
# так как f(x) монотонно возрастает
