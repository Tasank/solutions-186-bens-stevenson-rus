"""
Упражнение 63. Среднее значение.
В данном упражнении вы должны написать программу для подсчета среднего значения всех введенных пользователем чисел.
Индикатором окончания ввода будет служить ноль. При этом программа должна выдавать соответствующее сообщение об ошибке,
если первым же введенным пользователем значением будет ноль.
"""
numbers = []
# Бесконечный цикл пока не будет введена 0
while True:
    num = int(input('Введите число (0 для выхода): '))
    if num == 0:
        break
    numbers.append(num)

if numbers:
    average_value = sum(numbers) / len(numbers)
    print(f'Среднее значение - {average_value:.2f}')
else:
    print('Ошибка: не введено ни одного числа.')
