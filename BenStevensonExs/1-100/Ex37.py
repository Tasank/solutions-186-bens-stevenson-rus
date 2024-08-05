"""
Упражнение 37. Гласные и согласные.
Разработайте программу, запрашивающую у пользователя букву латинского алфавита.
Если введенная буква входит в следующий список (a, e, i, o или u), необходимо вывести сообщение о том,
что эта буква гласная. Если была введена буква y, программа должна написать, что эта буква может быть как гласной,
так и согласной. Во всех других случаях должно выводиться сообщение о том, что введена согласная буква.
"""
vowel_letters = ['a', 'e', 'i', 'o', 'u']

ask_alf = input('Введите букву латинского алфавита: ')

if len(ask_alf) == 1:
    if ask_alf in vowel_letters:
        print('Это гласная буква.')
    elif ask_alf == 'y':
        print('Эта буква может быть как гласной, так и согласной.')
    else:
        print('Введена согласная буква.')
else:
    print('Нужно ввести 1 букву латинского алфавита.')