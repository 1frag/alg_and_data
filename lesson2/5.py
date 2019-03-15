# 5. Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м
# включительно. Вывод выполнить в табличной форме:
# по десять пар «код-символ» в каждой строке.

# https://drive.google.com/file/d/14zUGHMy1Wr8Iv1lz0fRnAcA3Y75nNoMb/view?usp=sharing

for i in range(32, 127):
    if (i - 32) % 10 == 0:
        print('\n', end='')
    print('[{} - {}]'.format(i, chr(i)), end=' ')
