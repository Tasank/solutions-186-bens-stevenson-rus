"""
Упражнение 57. Счет за телефон.
Напишите программу, которая будет запрашивать у пользователя количество израсходованных за
месяц минут разговора и смс-сообщений и отображать базовую сумму тарификации,
сумму за дополнительные минуты и сообщения, сумму отчислений кол-центрам 911, налог, а также итоговую сумму к оплате.
При этом дополнительные звонки и сообщения необходимо выводить на экран только в случае их расходования.
Убедитесь в том, что все суммы отображаются в формате с двумя знаками после запятой.
"""
# Переменные (вводные) задачи
plan_sms = 50
plan_min = 50

base_price = 15.00

tax_911 = 0.44
tax_rate = 0.05

# Ввод
min_phone = int(input('Введите количество израсходованных минут: '))
sms_phone = int(input('Введите количество израсходованных сообщений: '))

# Вычисление дополнительных минут и сообщений
extra_min = max(0, min_phone - plan_min)
extra_sms = max(0, sms_phone - plan_sms)

# Вычисление стоимости дополнительных минут и сообщений
extra_min_cost = extra_min * 0.25
extra_sms_cost = extra_sms * 0.15

# Вычисление общей стоимости до налогообложения
subtotal = base_price + extra_min_cost + extra_sms_cost + tax_911

# Вычисление налога
tax = subtotal * tax_rate

# Вычисление итоговой суммы к оплате
total_price = subtotal + tax

# Вывод результатов
print()
print(f"Базовая сумма тарификации: ${base_price:.2f}")
if extra_min > 0:
    print(f"Сумма за дополнительные минуты: ${extra_min_cost:.2f}")
if extra_sms > 0:
    print(f"Сумма за дополнительные сообщения: ${extra_sms_cost:.2f}")
print(f"Сумма отчислений кол-центрам 911: ${tax_911:.2f}")
print(f"Налог: ${tax:.2f}")
print(f"Итоговая сумма к оплате: ${total_price:.2f}")
