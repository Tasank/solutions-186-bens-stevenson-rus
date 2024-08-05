"""
Упражнение 114. Отрицательные, положительные и нули.
Напишите программу, запрашивающую у пользователя целые числа, пока он не оставит строку ввода пустой.
После окончания ввода на экран должны быть выведены сначала все отрицательные числа, которые были введены,
затем нулевые и только после этого положительные. Внутри каждой группы числа должны отображаться в той
последовательности, в которой были введены пользователем.
"""

negatives =[]
zeros = []
positives = []

def ask():
    numbers = input('Введите число (Enter для выхода): ')
    while numbers != '':
        num = int(numbers)
        if num < 0:
            negatives.append(num)
        elif num == 0:
            zeros.append(num)
        else:
            positives.append(num)
        numbers = input('Введите число (Enter для выхода): ')

    for i in negatives:
        print('Отрицательные числа ->', i)
    for i in zeros:
        print('Нулевые числа ->', i)
    for i in positives:
        print('Положительные числа ->',i)

ask()

