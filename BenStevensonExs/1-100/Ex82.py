"""
Упражнение 82. Десятичное число в двоичное.
Напишите программу, которая будет преобразовывать десятичные значения (по основанию 10) в двоичные (по основанию 2).
Запросите целое число у пользователя и следуя алгоритму, приведенному ниже, преобразуйте его в двоичную запись.
По завершении выполнения программы в переменной result должно оказаться двоичное представление исходного числа.
Выведите результат на экран с соответствующим сообщением.
"""

num = int(input('Введите десятичное число: '))
result = ''
while num != 0:
    r = num % 2
    result += str(r)
    num = int(num / 2)
result =''.join(reversed(result))
print(result)