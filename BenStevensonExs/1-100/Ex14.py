"""
Упражнение 14. Рост.
Многие люди на планете привыкли рассчитывать рост человека в футах и дюймах,
даже если в их стране принята метрическая система. Напишите программу,
которая будет запрашивать у пользователя количество футов, а затем дюймов в его росте.
После этого она должна пересчитать рост в сантиметры и вывести его на экран.
"""
feet = int(input('Введите количество футов в вашем росте: '))
inch = int(input('Введите количество дюймов в вашем росте: '))

result = (feet * 30.48) + (inch * 2.54)
print(f'Рост в см - {result:.2f}')