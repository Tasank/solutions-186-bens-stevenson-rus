"""
Упражнение 155. Частота слов в файле.
Разработайте программу, которая будет показывать слово (или слова), чаще остальных встречающееся
в текстовом файле. Сначала пользователь должен ввести имя файла для обработки.
После этого вы должны открыть файл и проанализировать его построчно, разделив при этом строки по
словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов в
файле вам стоит игнорировать регистры.
"""
# Импортируем необходимые функции из модуля Ex117
from Ex117 import word


def frequent_words(filename):
    try:
        # Открываем файл для чтения
        with open(filename, 'r') as readfile:
            word_count = {}  # Словарь для подсчета частоты слов

            # Проходим по каждой строке в файле
            for line in readfile:
                # Приводим строку к нижнему регистру и разбиваем на слова
                words = word(line.lower())

                # Проходим по каждому слову в строке
                for w in words:
                    if w in word_count:
                        word_count[w] += 1  # Увеличиваем счетчик, если слово уже встречалось
                    else:
                        word_count[w] = 1  # Инициализируем счетчик, если слово встречается впервые

            # Находим максимальное значение частоты слов
            max_count = max(word_count.values())

            # Находим все слова, которые встречаются максимальное количество раз
            most_frequent_words = [w for w, count in word_count.items() if count == max_count]

            return most_frequent_words
    except FileNotFoundError:
        return 'Не удалось открыть файл.'


# Запрашиваем у пользователя имя файла
filename = input("Введите имя файла: ")
# Получаем список самых частых слов
most_frequent_words = frequent_words(filename)
# Выводим результат
print(f'Самое частое слово (слова): {most_frequent_words}')
