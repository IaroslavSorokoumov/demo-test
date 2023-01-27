# def gcd(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     print('Наибольший общий делитель:', a + b)
#
#
# gcd(4782, 698)

x1 = float(input('Введите X1: '))
y1 = float(input('Введите Y1: '))

x2 = float(input('Укажите X2: '))
y2 = float(input('Укажтите Y2: '))

x_diff = x1 - x2
y_diff = y1 - y2
print("Уравнение прямой, проходящей через эти точки:")
if x_diff == 0:
    print("Значение x =", x1)
elif y_diff == 0:
    print('Значение y =', y1)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("y = ", k, " * x + ", b)
