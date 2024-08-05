"""
Упражнение 83. Максимальное число в последовательности.
Это упражнение преследует цель идентификации количества смен максимального значения в коллекции случайных чисел.
Ряд должен быть заполнен числами от 1 до 100. При этом последовательность может содержать
дубликаты, а некоторых чисел из диапазона от 1 до 100 в ней может не быть.
"""
from random import randrange

a = randrange(1,101)
num_max = a
count = 0

print('Первое число: ', num_max)
for i in range(1,100):
    a = randrange(1,101)
    if a > num_max:
        num_max = a
        count += 1
        print('%d <== Обновление' % num_max)
    else:
        print(a)
print('Максимальное значение в ряду: ', num_max)
print('Количество смен максимального значения: ', count)