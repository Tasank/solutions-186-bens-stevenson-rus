"""
Упражнение 179. Рекурсивный квадратный корень.
Напишите функцию вычисления квадратного корня с двумя входными параметрами.
Первый из них – n – будет характеризовать число, из которого вычисляется квадратный корень,
а второй – guess – текущее приближение при его вычислении. Значение параметра guess по умолчанию примем за 1,0.
У первого параметра значения по умолчанию быть не должно.
Функция вычисления корня должна быть рекурсивной.
"""
def recursive_square_root(n, guess=1.0):
    # Если заменить 1 ** -12 на 1e-12 выйдет ошибка
    if abs(guess**2 - n) < 1 ** -12:
        return guess
    else:
        new_guess = (guess + n / guess) / 2
        return recursive_square_root(n, new_guess)

def main():
    # Несколько тестовых запусков
    test_values = [4, 133, 16, 25, 100, 12345]
    for value in test_values:
        print(f'Квадратный корень ({value}): {recursive_square_root(value)}')

if __name__ == "__main__":
    main()