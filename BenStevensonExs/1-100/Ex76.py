"""
Упражнение 76. Многословные палиндромы.
Напишите программу, запрашивающую у пользователя фразу и при помощи цикла определяющую,
является ли она палиндромом.
Примечание*
Обработка русских слов
"""
ask = input('Напишите свою фразу: ')
reversed_ask = ''
# Обработка пробелов
s = ask.replace(' ','')
s = s.lower()
for i in range(len(s), 0, -1):
    if s[i-1] >= 'а' and s[i-1] <= 'я':
        reversed_ask += s[i-1]
if s == reversed_ask:
    print('ПАЛИНДРОМ!!!')
else:
    print("не палиндром :(")