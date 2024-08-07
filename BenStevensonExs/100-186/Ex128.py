"""
Упражнение 128. Подсчитать элементы в списке.
В данном упражнении вы создадите новую функцию countRange, которая будет подсчитывать количество элементов в списке,
значения которых больше или равны заданному минимальному порогу и меньше максимального. Функция должна принимать три
параметра: список, минимальную границу и максимальную границу. Возвращать она будет целочисленное значение, большее или
равное нулю. В основной программе реализуйте демонстрацию вашей функции для нескольких списков с разными минимальными и
максимальными границами. Удостоверьтесь, что программа будет корректно работать со списками, содержащими как
целочисленные значения, так и числа с плавающей запятой.
"""


def countRange(data, min_value, max_value):
    count = 0
    for i in data:
        if min_value <= i < max_value:
            count += 1
    return count

def main():
    data = [1, 2, 3, 4, 5, 5.5, 6, 7, 8, 9, 10]
    print('Несколько элементов входят в диапазон. От 2 до 8.')
    print(f'Результат: {countRange(data, 2 , 8)}')
    print()


    data = [1.0, 2.0, 3.5, 3.1, 3.9, 9.9]
    print('Диапазон элементов с плавающей точкой. От -20 до 20.')
    print(f'Результат: {countRange(data, -20 , 20)} | Ожидание: 6 элементов |')
    print()

    data = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3]
    print('Диапазон повторяющихся элементов. От -1 до 4')
    print(f'Результат: {countRange(data, -1, 4)} | Ожидание: 9 элементов |')
    print()

    data = []
    print('Пустой список. От 0 до 100')
    print(f'Результат: {countRange(data, -1, 4)} | Ожидание: 0 элементов |')
    print()

main()