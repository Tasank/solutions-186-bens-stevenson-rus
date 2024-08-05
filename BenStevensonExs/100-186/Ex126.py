"""
Упражнение 126. Раздача карманных карт.
Напишите функцию deal, принимающую на вход три параметра: количество игроков, количество раздаваемых каждому из них
карт и саму колоду. Функция должна возвращать список рук, которые были розданы игрокам. При этом каждая рука,
в свою очередь, тоже является списком из входящих в нее карт.
Во время раздачи карт игрокам функция параллельно должна удалять розданные карты из переданной ей третьим параметром
колоды. Также принято раздавать карты каждому игроку по одной строго по очереди.
Придерживайтесь этих принципов и при написании своей функции.
Воспользуйтесь своими наработками из упражнения 125 при построении структуры основной программы
"""
from Ex125 import *

deck = createDeck()
shuffle(deck)
def deal(players, card, deck):
    # Список карманных карт игроков
    hands = [[]for x in range(players)]
    for i in range(card):
        for hand in hands:
            # Добавляем игрокам карты и удаляем их из колоды
            hand.append(deck.pop())
    return hands

hands = deal(4, 5, deck)
# i - индекс, hand - значение
# Вывод карт игроков
for i, hand in enumerate(hands):
    print(f" Игрок № {i + 1} колода: {hand}")
print(f"Оставшиеся карты в колоде: {deck}")
