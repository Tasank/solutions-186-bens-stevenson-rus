"""
Упражнение 111. Обратный порядок.
Напишите программу, которая, как и в предыдущем случае, будет запрашивать у пользователя целые числа и сохранять их
в виде списка. Индикатором окончания ввода значений также должен служить ноль. На этот раз необходимо вывести на экран
введенные значения в порядке убывания.
"""
def sort_list(li):
    li.sort()
    li.reverse()
    return li

def ask():
    l = []
    num = int(input('Введите число (0 для выхода): '))
    while num != 0:
        l.append(num)
        num = int(input('Введите число (0 для выхода): '))
    # Вывод элементов списка, построчно
    print('Отсортированный список в порядке убывания: ')
    for i in sort_list(l):
        print(i)

ask()