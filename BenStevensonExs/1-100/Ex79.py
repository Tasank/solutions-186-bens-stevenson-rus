"""
Упражнение 79. Наибольший общий делитель.
Напишите программу, запрашивающую у пользователя два положительных целых числа и
выводящую для них наибольший общий делитель.
"""
print("Наибольший общий делитель.")
n = int(input('Введите первое целое число: '))
m = int(input('Введите второе целое число: '))
# Инициализируйте переменную d меньшим из чисел n и m
if n > m:
    d = m
else:
    d = n

while n % d != 0 or m % d != 0:
    d -= 1

print('Наибольший общий делитель равен :',d)

