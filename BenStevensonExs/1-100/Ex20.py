"""
Упражнение 20. Уравнение состояния идеального газа.
Напишите программу для измерения количества газа в молях при заданных пользователем давлении, объеме и температуре.
Проверьте свою программу путем вычисления количества газа в баллоне для дайвинга.
Типичный баллон вмещает 12 л газа под давлением 20 000 000 Па (примерно 3000 фунтов на кв. дюйм).
Температуру в комнате примем за 20° по шкале Цельсия или 68° по Фаренгейту.
"""
R = 8.314

P = float(input('Введите давление в паскалях: '))
V = float(input('Введите объем в литрах: '))

# Переводим температуру в Кельвин в зависимости от шкалы
ask = input('Шкала температуры будет по шкале Фаренгейта? (да/нет): ')

if ask.lower() == 'да':
    t = float(input('Введите температуру по шкале Фаренгейта: '))
    T = ((t - 32) * (5 / 9)) + 273.15
else:
    t = float(input('Введите температуру по шкале Цельсия: '))
    T = t + 273.15

n = (P * V) / (R * T)
print('Количество газа в молях при заданных пользователем данных: ', n)