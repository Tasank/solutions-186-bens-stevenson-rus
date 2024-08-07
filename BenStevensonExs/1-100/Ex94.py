"""
Упражнение 94. Треугольник ли?
Напишите функцию для определения возможности построения треугольника на основании длин трех его потенциальных сторон.
Функция должна принимать три числовых параметра и возвращать булево значение. Если длина хотя бы одной из трех сторон
меньше или равна нулю, функция должна вернуть False. В противном случае необходимо выполнить проверку на допустимость
построения треугольника на основании введенных длин сторон и вернуть соответствующее значение.
Напишите основную программу, запрашивающую у пользователя длины сторон и выводящую на экран информацию о том,
может ли при заданных значениях получиться треугольник.
"""
def check(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a < (b + c):
        if b < (a + c):
            if c < (a + b):
                return True
    else:
        return False

def main():
    a = int(input('Введите 1 сторону вашего возможного треугольника: '))
    b = int(input('Введите 2 сторону вашего возможного треугольника: '))
    c = int(input('Введите 3 сторону вашего возможного треугольника: '))
    if check(a, b, c):
        print('При заданных значениях может получиться треугольник!')
    else:
        print('Треугольник невозможен')
main()