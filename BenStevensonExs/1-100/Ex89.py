"""
Упражнение 89. Переводим целые числа в числительные.
Такие слова, как первый, второй, третий, являются числительными. В данном упражнении вам необходимо написать функцию,
принимающую на вход в качестве единственного аргумента целое число и возвращающую строковое значение,
содержащее соответствующее числительное (на английском языке). Ваша функция должна обрабатывать числа в диапазоне
от 1 до 12. Если входящее значение выходит за границы этого диапазона, вывод должен оставаться пустым.
В основной программе запустите цикл по натуральным числам от 1 до 12 и выведите на экран соответствующие им числительные
Ваша программа должна запускаться только в том случае, если она не импортирована в виде модуля в другой файл.
"""

def slation(n):
    text = ''
    account = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tenth', 'eleventh',
          'twelfth']
    if n >= 12 or n < 0:
        return
    text = account[n]
    print(text)
def main():
    for i in range(1, 12):
        slation(i)