"""
Упражнение 34. Вчерашний хлеб.
Напишите программу, которая будет запрашивать у пользователя количество приобретенных вчерашних буханок хлеба.
В вывод на экран должны быть включены обычная цена за буханку, цена со скидкой и общая стоимость приобретенного хлеба.
Все значения должны быть выведены на отдельных строках с соответствующими описаниями.
Используйте для вывода формат с двумя знаками после запятой и выровненным разделителем.
"""
bread_price = 3.49
discount = 0.6
discounted_price = bread_price * (1 - discount) # Умножить  на 0.4

old_bread = int(input('Введите количество приобретенных вчерашних буханок хлеба: '))

total_cost = old_bread * discounted_price

print(f'Обычная цена за буханку: {bread_price} $')
print(f'Цена со скидкой: {discounted_price:.2f} $')
print(f'Общая стоимость приобретенного хлеба: {total_cost:.2f} $')