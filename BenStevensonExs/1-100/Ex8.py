"""
Упражнение 8. Сувениры и безделушки.
Напишите программу, запрашивающую у пользователя количество тех и других покупок,
после чего выведите на экран общий вес посылки.
"""

souvenir_weight = 75
trinkets_weight = 112

souvenir = int(input('Введите кол-во приобретённых сувениров: '))
trinkets = int(input('Введите кол-во приобретённых безделушек: '))

total = (souvenir * souvenir_weight) + (trinkets * trinkets_weight)
print(f'Общий вес посылки: {total} граммов')