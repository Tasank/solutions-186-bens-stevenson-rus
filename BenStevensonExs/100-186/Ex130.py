"""
Упражнение 130. Унарные и бинарные операторы.
Напишите функцию для поиска унарных операторов + и – в списке лексем и их замены на сочетание символов
u+ и u– соответственно. Функция должна принимать в качестве единственного параметра список лексем математического
выражения и возвращать его копию с произведенной заменой унарных операторов. Оператор + или – можно идентифицировать
как унарный в одном из двух случаев: если он идет первым в списке или если ему предшествует другой оператор либо
открывающая скобка. Во всех остальных случаях оператор может считаться бинарным.
В основной программе продемонстрируйте работу функции. Запросите у пользователя строку с математическим выражением,
разбейте ее на лексемы, выделите в отдельный список унарные операторы и выведите их на экран.
"""
from Ex129 import tokenlist

def If_Unary_Operator(list_tokens):
    result = []
    for i in range(len(list_tokens)):
        # Если первый оператор + или - это унарный оператор
        if i == 0 and (list_tokens[i] == '-' or list_tokens[i] == '+'):
            result.append("унарный" + list_tokens[i])
        # Унарный оператор если предыдущая лексема была оператором или открывающей скобкой
        elif i > 0 and (list_tokens[i] == '-' or list_tokens[i] == '+') and \
            (list_tokens[i-1] == '*' or list_tokens[i-1] == '/' or list_tokens[i-1] == '^'
             or list_tokens[i - 1] == '('):
            result.append("унарный" + list_tokens[i])
        # Если не унарный добавляем в список без изменений
        else:
            result.append(list_tokens[i])
    # Возвращаем новый список
    return result

def main():
    text = input('Введите математическое выражение: ')
    tokens = tokenlist(text)
    print(f'Лексемы: {tokens}')
    print()
    total = If_Unary_Operator(tokens)
    print(f'Поиск унарных операторов: {total}')

if __name__ == '__main__':
    main()