"""
Упражнение 74. Квадратный корень.
Напишите программу, реализующую метод Ньютона для нахождения квадратного корня числа x,
введенного пользователем.
"""
x = int(input('Введите число: '))
guess = x / 2
while guess * guess - x > 10e-12: # можно просто поставить 0 вместо 10e-12, ответ не изменится
    guess = (guess + x / guess) / 2

print('Результат: ', guess)
