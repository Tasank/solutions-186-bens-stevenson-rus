"""
Упражнение 59. Следующий день.
Разработайте программу, принимающую на вход дату и выводящую на экран дату, следующую за ней.
Например, если пользователь введет дату, соответствующую 18 ноября 2019 года, на экран должен быть
выведен следующий день, то есть 19 ноября 2019 года. Если входная дата будет представлять 30 ноября,
то на выходе мы должны получить 1 декабря. И наконец, если ввести последний день года – 31 декабря 2019-го,
пользователь должен увидеть на экране дату 1 января 2020-го. Дату пользователь должен вводить в три этапа: год,
месяц и день. Убедитесь, что ваша программа корректно обрабатывает високосные годы.
"""
from Ex58 import check_year

months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль",
          "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

month_days = {
    'январь': 31, 'февраль': 28, 'март': 31, 'апрель': 30,
    'май': 31, 'июнь': 30, 'июль': 31, 'август': 31,
    'сентябрь': 30, 'октябрь': 31, 'ноябрь': 30, 'декабрь': 31
}

print('Введите интересующую дату.')

# Ввод даты
day = int(input('Введите день: '))
month = input('Введите название месяца: ').strip().lower()
year = int(input('Введите год: '))

# Сразу проверяем что месяц и день правильные
if month not in month_days or not (1 <= day <= month_days[month]):
    print('Ошибка ввода.')

else:
    # Учет високосного года
    if month == 'февраль' and check_year(year):
        month_days['февраль'] = 29

    # Проверка перехода на следующий день
    if day < month_days[month]:
        print(f'Следующий день: {day + 1} - {month} - {year} год.')
    else:
        # (... % 12) нужно чтобы с декабря переход на январь, а не просто был индекс + 1
        # months.index('декабрь') равняется 11, то есть (11 + 1) % 12 будет индекс 0, а это январь
        next_month_index = (months.index(month) + 1) % 12
        # Год + 1 если индекс следующего месяца равняется 0 (декабрь)
        next_year = year + (1 if next_month_index == 0 else 0)
        print(f'Следующий день: 1 - {months[next_month_index]} - {next_year} год.')
