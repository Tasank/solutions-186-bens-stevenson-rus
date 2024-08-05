"""
Упражнение 186. Кодирование на основе длин серий.
Напишите рекурсивную функцию, реализующую алгоритм кодирования на основе длин серий,
описанный в упражнении 185. На вход функции должен поступать список или строка,
а на выходе будет закодированный список. В основной программе запросите у пользователя строку,
сожмите ее при помощи своей функции и отобразите на экране кодированный список.
"""
def encoding_list(data):
    # Базовый случай
    if not data:
        return []

    element = data[0]
    count = 1

    # Считаем количество повторов текущего элемента
    # Пока счётчик меньше длинны строки и первый элемент строки равняется элементу счётчика, счётчик + 1
    while count < len(data) and data[count] == element:
        count += 1
    # Рекурсивный возврат
    return [element, count] + encoding_list(data[count:])

# Основная программа
def main():
    user_input_data = input("Введите строку для сжатия: ")

    encoded_data = encoding_list(user_input_data)
    print(encoded_data)

if __name__ == "__main__":
    main()