"""
Упражнение 4. Площадь садового участка.
Создайте программу, запрашивающую у пользователя длину и ширину садового участка в футах.
Выведите на экран площадь участка в акрах.
В одном акре содержится 43 560 квадратных футов.
"""
length = float(input("Введите длину садового участка в футах: "))
width = float(input("Введите ширину садового участка в футах: "))

result = length * width / 43560

print('Площадь садового участка в акрах равна %.2f ' % result)