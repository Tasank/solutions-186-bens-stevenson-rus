"""
Упражнение 105. Произвольные системы счисления.
Напишите программу, которая позволит пользователю преобразовывать числа из одной системы счисления в другую
произвольным образом. Ваша программа должна поддерживать все системы счисления в диапазоне от 2 до 16 как для входных,
так и для выходных данных. Если пользователь выберет систему с основанием, выходящим за границы допустимого,
на экран должна быть выведена ошибка. Разделите код программы на несколько функций, включая функцию,
конвертирующую число из произвольной системы счисления в десятичную, и обратную функцию, переводящую значение из
десятичной системы в произвольную.
"""

def system(original_system, base_system, number):
    if original_system > 16 or original_system < 2:
        return 'Ошибка'
    # Используем метод волшебника 1) сначала переводим любую систему счисления в 10-ую
    # 2) После 10-ую преобразовываем в новую систему
    result = back_convert_10(number, original_system)
    result = convert_10(result, base_system)
    return result

# Произвольная система счисления в десятичное число
# Второй аргумент это основание системы счисления самого числа
def back_convert_10(number, base):
    result = int(number, base)
    return result

# Из десятичной системы исчисления в любую
def convert_10(value, base):
    digits = '0123456789abcdefghijklmopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while value > 0:
        result = digits[value % base] + result
        value //= base
    return result

def display():
    print('________Конвертация систем счисления________')
    print('           (2)   (8)   (10)   (16)          ')
    print('Введите число интересующий системы счисления.')
    print('_____________________________________________')
    # Ввод
    original = int(input('Введите изначальную систему счисления: '))
    base = int(input('Введите новую систему счисления: '))
    number = (input('Введите число для преобразования: '))
    # Вывод
    print('____________________________________')
    print('Ваш результат:', system(original, base, number))
display()