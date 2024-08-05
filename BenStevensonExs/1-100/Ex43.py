"""
Упражнение 43. Узнать ноту по частоте
В предыдущем упражнении мы определяли частоту ноты по ее названию и номеру октавы. Теперь выполним обратную операцию.
Запросите у пользователя частоту звука. Если введенное значение укладывается в диапазон ±1 Гц от значения в таблице,
выведите на экран название соответствующей ноты. В противном случае сообщите пользователю, что ноты,
соответствующей введенной частоте, не существует. В данном упражнении можно ограничиться только нотами,
приведенными в таблице. Нет необходимости брать в расчет другие октавы.
"""

frequency = float(input('Введите частоту (в Гц): '))

# Проверка каждой ноты
if 260.63 <= frequency <= 262.63:
    note = 'C4'
elif 292.66 <= frequency <= 294.66:
    note = 'D4'
elif 328.63 <= frequency <= 330.63:
    note = 'E4'
elif 348.23 <= frequency <= 350.23:
    note = 'F4'
elif 391.00 <= frequency <= 393.00:
    note = 'G4'
elif 439.00 <= frequency <= 441.00:
    note = 'A4'
elif 492.88 <= frequency <= 494.88:
    note = 'B4'
else:
    note = None


if note:
    print(f'Частота {frequency:.2f} Гц соответствует ноте {note}')
else:
    print('Ноты, соответствующей введенной частоте, не существует.')
