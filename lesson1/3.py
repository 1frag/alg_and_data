# 3. По введенным пользователем координатам двух
# точек вывести уравнение прямой, проходящей через эти точки.

# https://drive.google.com/file/d/14dCJEqivznVXVznO0lIc-mLUuPT0NoNl/view?usp=sharing

# Формат ввода:
# x1 y1
# x2 y2
import sys

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
if x1 == x2:
    print('x={}'.format(x1))
    sys.exit()
k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
if b > 0:
    print('y={}*x+{}'.format(k, b))
else:
    print('y={}*x-{}'.format(k, -b))