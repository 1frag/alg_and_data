# 2. Написать два алгоритма нахождения i-го по счёту, i <= 100 000
# простого числа. Первый - использовать алгоритм
# решето Эратосфена. Второй - без использования
# "решета". Проанализировать скорость и сложность алгоритмов.
import cProfile


def with_sieve(n):
    max_n = 10000000
    is_prime = [1 for _ in range(max_n)]
    for i in range(2, max_n):
        if not is_prime[i]:
            continue
        n -= 1
        if n == 0:
            return i
        for j in range(i*i, max_n, i):
            is_prime[j] = 0


def check_prime(n):
    stop = int(n ** 0.5)
    for i in range(2, stop+1):
        if n % i == 0:
            return False
    return True


def without_sieve(n):
    max_n = 10000000
    for i in range(2, max_n):
        if check_prime(i):
            n -= 1
            if n == 0:
                return i


def test(func):
    answer = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i, x in enumerate(answer):
        if x != func(i+1):
            print(f'{i}-тое простое число найдено неверно')
        else:
            print('OK!')


# test(with_sieve)
# test(without_sieve)
K = 100000
# print(with_sieve(K))
# print(without_sieve(K))

cProfile.run(f"with_sieve({K})")     # 5 function calls in 2.599 seconds
cProfile.run(f"without_sieve({K})")  # 1299712 function calls in 13.750 seconds

# Разница для K = 100000 весьма ощутима более 10 секунд!
# Асимптотика решета: O(N*log(logN)) (почти линия)
# Асимптотика без решета: O(N ** 1.5) (почти квадрат)
