"""
Упражнение 138. Текстовые сообщения.
Напишите программу, отображающую последовательность кнопок, которую необходимо нажать,
чтобы на экране телефона появился текст, введенный пользователем. Создайте словарь, сопоставляющий символы с кнопками,
которые необходимо нажать, а затем воспользуйтесь им для вывода на экран последовательности кнопок в соответствии с
введенным пользователем сообщением по запросу. Например, на ввод строки Hello, World! ваша программа должна откликнуться
следующим выводом: 443355 5555666110966677755531111. Удостоверьтесь, что ваша программа корректно обрабатывает
строчные и прописные буквы. При преобразовании букв в цифры игнорируйте символы, не входящие в указанный перечень,
такие как точка с запятой или скобки.
"""
def display():
    print('Символы, соответствующие  кнопкам на старых телефонах')
    print('Кнопка | Символы')
    print('1	   |. , ? ! :')
    print('2	   |A B C')
    print('3	   |D E F')
    print('4	   |G H I')
    print('5	   |J K L')
    print('6	   |M N O')
    print('7	   |P Q R S')
    print('8	   |T U V')
    print('9	   |W X Y Z')
    print('0	   | Пробел')
    print('________________')


buttons = {'1': '.,?!:', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO',
           '7': 'PQRS', '8': 'TUV', '9': 'WXYZ', '0': ' '}
# Объявляем обратный словарь, где например ключ С будет иметь значение - 222
char_to_button = {}
for button, chars in buttons.items():
    for index, char in enumerate(chars):
        char_to_button[char] = button * (index + 1)

def upgrade(text):
    result = []
    for char in text.upper(): # Приводим текст к верхнему регистру для соответствия словарю
        if char in char_to_button:
            result.append(char_to_button[char])
    return ''.join(result)
def main():
    display()
    ask = input('Введите текст: ')
    total = upgrade(ask)
    print(total)
main()

