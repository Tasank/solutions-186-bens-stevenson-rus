"""
Упражнение 85. Вычисляем длину гипотенузы.
Напишите функцию, принимающую на вход длины двух катетов прямоугольного треугольника и
возвращающую длину гипотенузы, рассчитанную по теореме Пифагора.
В главной программе должен осуществляться запрос длин сторон у пользователя,
вызов функции и вывод на экран полученного результата.
"""
from math import sqrt

def hypotenuse():
    one_len = int(input('Введите длину первого катета: '))
    two_len = int(input('Введите длину второго катета: '))
    c = sqrt(one_len ** 2 + two_len ** 2)
    print('Длина гипотенузы равна: ', c)
hypotenuse()