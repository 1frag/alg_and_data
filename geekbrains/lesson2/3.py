# 3. Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.

# https://drive.google.com/file/d/1Cld1HLkdcDIaveimkBvHKDo25nH6TcPg/view?usp=sharing

n = int(input('Введите натуральное число: '))
m = 0
while n:
    m *= 10
    m += n % 10
    n //= 10
print('Ответ на задачу: {}'.format(m))
