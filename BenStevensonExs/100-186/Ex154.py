"""
Упражнение 154. Частота букв в файле.
Напишите программу, которая будет способствовать дешифрации текста путем вывода на экран частоты появления разных букв.
При этом пробелы, знаки препинания и цифры должны быть проигнорированы.
Также не должен учитываться регистр, то есть символы a и A должны восприниматься как одна буква.
Имя файла для анализа пользователь должен передавать программе посредством аргумента командной строки.
Если программе не удастся открыть файл для анализа или аргументов командной строки будет слишком много,
на экране должно быть отображено соответствующее сообщение об ошибке.
"""
import sys

def main():
    # Если аргументов командной строки слишком много, то вывести ошибку
    if len(sys.argv) != 2:
        print('Аргументов командной строки слишком много или недостаточно.')
        return

    # Получение имени файла из аргумента командной строки
    filename = sys.argv[1]

    # Если не удастся открыть файл для анализа, то вывести ошибку
    try:
        with open(filename, 'r') as readfile:
            text = readfile.read()
    except IOError:
        print('Не удалось открыть файл')
        return
    # Привести к нижнему регистру
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))  # фильтрация только букв

    # Подсчет частоты букв
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    # Метод .items() возвращает представление словаря в виде последовательности кортежей (ключ, значение)
    # sorted() -  сортирует кортежи (ключ, значение) из словаря frequency по ключам (буквам) в алфавитном порядке.
    for char, count in sorted(frequency.items()):
        print(f'{char}: {count}')

if __name__ == '__main__':
    main()