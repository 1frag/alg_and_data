# 6. Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.

# работа с ангийским алфавитом
a = int(input('Введите номер от 1 до 26:\n'))
print('Это буква - {}'.format(chr(ord('a') + a - 1)))
