"""
Упражнение 96. Является ли строка целым числом?
В данном упражнении вам предстоит написать функцию с именем isInteger, определяющую,
представляет ли введенная строка целочисленное значение. При проверке вы можете игнорировать ведущие и
замыкающие пробелы в строке. После исключения лишних пробелов строку можно считать представляющей целое число,
если ее длина больше или равна одному символу и она целиком состоит из цифр.
Возможен также вариант с ведущим знаком «+» или «-», после которого должны идти цифры.
В основной программе у пользователя должна запрашиваться исходная строка и выводиться сообщение о том,
можно ли введенное значение воспринимать как целое число. Убедитесь, что основная программа не будет запускаться,
если файл импортирован в другой файл в качестве модуля.
"""
def isInteger(n):
    # Удаляем пробелы в начале и конце
    n = n.strip()
    # isdigit возвращает True если строка в ней является цифрой
    if (n[0] == "+" or n[0] == '-') and n[1:].isdigit():
        return True
    if n.isdigit():
        return True
    return False

def main():
    number = input('Введите число: ')
    if isInteger(number):
        print('(%s) - можно воспринимать как целое число' % number)
    else:
        print('Это не целое число.')
# Вызываем функцию, только если файл не импортирован
if __name__ == '__main__':
    main()