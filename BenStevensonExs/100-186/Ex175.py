"""
Упражнение 175. Рекурсивный перевод числа из десятичного в двоичное.
Напишите основную программу, которая будет использовать рекурсивную функцию для преобразования неотрицательного числа,
введенного пользователем, из десятичной системы счисления в двоичную. Если будет введено отрицательное значение,
программа должна вывести соответствующее сообщение об ошибке.
"""
# Рекурсивная функция преобразования
def transformation(num):
    if num < 0:
        return "Введите неотрицательное число"
    elif num == 0 or num == 1:
        return str(num)
    else:
        transformation(num // 2) + str(num % 2)
# Основная программа. Вывод результата
def main():
    try:
        num = int(input("Введите неотрицательное целое число: "))
        print(f"Двоичное представление числа {num}: {transformation(num)}")
    except ValueError:
        print("Ошибка: введите целое число.")

if __name__ == "__main__":
    main()