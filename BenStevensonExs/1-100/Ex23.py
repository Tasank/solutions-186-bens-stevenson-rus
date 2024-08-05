"""
Упражнение 23. Площадь правильного многоугольника.
Напишите программу, которая будет запрашивать у пользователя значения переменных s и n и выводить на
экран площадь правильного многоугольника, построенного на основании этих величин
"""
from math import tan
from math import pi

s = int(input('Введите длину сторон многоугольника: '))
n = int(input('Введите кол-во сторон многоугольника: '))

area = (n * (s ** 2)) / (4 * tan(pi / n))
print(f'Площадь правильного многоугольника {area:.2f}')