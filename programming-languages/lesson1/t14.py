# 4. Напишите программу, которая считывает из потока ввода таблицу
# со следующими столбцами: ФИО, сумма кредита, долг. Затем из
# таблицы исключить все закрытые кредиты (долг равен нулю). Для
# всех оставшихся начислить пеню в размере 42% от суммы долга.
# После этого, программа выводит на экран изменённую таблицу.
""" Конец считывания после пустой строки """


def collect(data=[]):
    data.append(input().split())
    return (data[-1] and collect()) or data[:-1]


def increase(item):
    item[3] = '%.2f' % (int(item[3]) * 1.42)
    return ' '.join(item)


def main():
    return '\n'.join(map(increase, filter(lambda x: int(x[-1]), collect())))


if __name__ == '__main__':
    print(main())

"""
Tatiana Santos 411889 36881
Yuvraj Holden 121877 0
Theia Nicholson 783887 591951
Raife Padilla 445511 0
Hamaad Millington 818507 276592
Maksim Whitehead 310884 0
Iosif Portillo 773233 0
Lachlan Daniels 115100 0
Evie-Grace Reese 545083 0
Ashlea Cooper 68771 0


Serenity Villa 987279 0
Yuvraj Oakley 972087 0
Malik Kelley 9741 0
Mahek Whittington 11344 0
Anabel Keeling 355090 0


"""
