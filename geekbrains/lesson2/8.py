# 8. Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются
# вводом с клавиатуры.

# https://drive.google.com/file/d/1kCKSdIpqCEGpIJHZGhpIkcte3MFu-CCw/view?usp=sharing

c = input('Какую цифру будем искать: ')
n = int(input('Сколько чисел в последовательности: '))
ans = 0
for _ in range(n):
    a = input('Введите число: ')
    ans += a.count(c)
print(ans)
