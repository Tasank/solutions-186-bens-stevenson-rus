"""
Упражнение 32. Сумма цифр в числе
Разработайте программу, запрашивающую у пользователя целое четырехзначное число и
подсчитывающую сумму составляющих его цифр.
Например, если пользователь введет число 3141, программа должна вывести следующий результат: 3 + 1 + 4 + 1 = 9.
"""
number = input('Введите целое четырехзначное число: ')
total = int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])
# Другой вариант total = sum(int(digit) for digit in number)
print(f'Сумма цифр в числе - {total}')