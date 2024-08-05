"""
Упражнение 113. Избавляемся от дубликатов.
В данном упражнении вам предстоит разработать программу, в которой у пользователя будет запрошен список слов,
пока он не оставит строку ввода пустой. После этого на экране должны быть показаны слова, введенные пользователем,
но без повторов, – каждое по одному разу. При этом слова должны быть отображены в том же порядке,
в каком их вводили с клавиатуры
"""

def sort_ask(ask):
    return list(set(ask))
def ask():
    words = []
    word = input('Введите слово (Enter для выхода): ')
    while word != "":
        words.append(word)
        word = input('Введите слово (Enter для выхода): ')
    print(*sort_ask(words))

ask()