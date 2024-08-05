"""
Упражнение 78. Гипотеза Коллатца.
Напишите программу, которая будет запрашивать у пользователя целое
число и выводить все числа, начиная с введенного числа и заканчивая
единицей. После этого пользователь должен иметь возможность ввести
другое число и снова получить ряд чисел, называемый сиракузской последовательностью.
Условием выхода из программы должен быть ввод
пользователем нуля или отрицательного числа
"""
print('Программа выведет сиракузкую последовательность')
first_num = int(input('Введите целое число: '))
# Для интереса добавил счётчик, чтобы было видно сколько совершенно итераций
count = 0
while first_num > 0:
    while first_num != 1:
        if first_num % 2 == 0:
            first_num = int(first_num / 2)
        else:
            first_num = first_num * 3 + 1
        count += 1
        print('Текущее число: ', first_num)
    print('Всего было - %d попыток вычислений.' % count)
    print('-------------------------------------------')
    count = 0
    first_num = int(input('Введите целое число (Для выхода введите любое число меньше 1): '))
print()
print('Выход из программы.')

