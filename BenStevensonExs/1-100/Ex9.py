"""
Упражнение 9. Сложные проценты.
Представьте, что вы открыли в банке сберегательный счет под 4 % годовых.
Проценты банк рассчитывает в конце года и добавляет к сумме счета.
Напишите программу, которая запрашивает у пользователя сумму первоначального депозита,
после чего рассчитывает и выводит на экран сумму на счету в конце первого, второго и третьего годов.
Все суммы должны быть округлены до двух знаков после запятой.
"""
initial_deposit = float(input('Введите сумму первоначального депозита: '))
annual_interest_rate = 0.04

# Рассчитываем сумму на счету в конце каждого года
for year in range(1, 4):
    initial_deposit += initial_deposit * annual_interest_rate
    print(f'Сумма в конце {year}-го года: {initial_deposit:.2f}')