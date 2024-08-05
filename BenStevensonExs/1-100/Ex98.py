"""
Упражнение 98. Простое число?
Напишите функцию для определения того, является ли введенное число простым. Возвращаемое значение должно быть либо True,
 либо False. В основной программе, как и ожидается, пользователь должен ввести целое число и получить ответ о том,
 является ли оно простым. Убедитесь, что основная программа не будет запускаться,
 если файл импортирован в другой файл в качестве модуля.
"""
def simple_num(n):
    if n > 1 and n % n == 0 and n % 1 == 0:
        return True
    else:
        return False

def main():
    n = int(input('Введите число: '))
    if simple_num(n):
        print('Число простое!')
    else:
        print('Число не является простым!')

if __name__ == '__main__':
    main()