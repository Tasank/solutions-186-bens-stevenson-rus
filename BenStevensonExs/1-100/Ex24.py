"""
Упражнение 24. Единицы времени.
Создайте программу, в которой пользователь сможет ввести временной промежуток в виде количества дней, часов,
минут и секунд и узнать общее количество секунд, составляющее введенный отрезок.
"""
DD = int(input('Введите количества дней: '))
HH = int(input('Введите количества часов: '))
MM = int(input('Введите количества минут: '))
SS = int(input('Введите количества секунд: '))

total = (DD * 86400) + (HH * 3600) + (MM * 60) + SS
print('Общее количество секунд: ', total)