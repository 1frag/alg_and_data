# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран
# это число и сумму его цифр.


def sum_digits(a):
    res = 0
    while a:
        res += a % 10
        a //= 10
    return res


lst = map(int, input('Введите все числа через пробел:\n').split())  # Формируем список из введенных чисел
ans = [max(lst, key=sum_digits)] * 2  # поиск максимального из списка по ключу значения функции
ans[1] = sum_digits(ans[1])  # формируем список для ответа
print('Искомое число {} сумма его цифр {}'.format(*ans))  # выводим ответ

# основная алгоритмическая часть лежит в функции ее блок-схема:
# https://drive.google.com/file/d/1pjiZCQT-Q0Kt36INKzRNdDQh2qwVSNNv/view?usp=sharing
# остальная часть программы прокомментирована и совсем не интересно выглядит в виде блок-схемы
