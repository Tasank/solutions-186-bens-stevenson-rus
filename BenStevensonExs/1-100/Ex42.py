"""
Упражнение 42. Узнать частоту по ноте.
Пусть ваша программа запрашивает у пользователя обозначение ноты и показывает ее частоту согласно приведенной таблице.
После этого вы можете доработать свою программу таким образом, чтобы она поддерживала все октавы,
начиная от субконтроктавы (C0) до пятой октавы (C8). И хотя можно это реализовать путем добавления бесконечного
количества блоков if, это будет довольно громоздким, недостаточно элегантным и просто неприемлемым решением данной
задачи
"""
# Частоты нот одной октавы
note_frequencies = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88
}

note_input = input('Введите ноту (например, C4, D3, F2): ')

# Извлечение
note = note_input[:-1]  # буква ноты
octave = int(note_input[-1])  # номер октавы

# Проверка наличия ноты в словаре
if note in note_frequencies:
    # Частота ноты в указанной октаве
    frequency = note_frequencies[note] / (2 ** (4 - octave))
    print(f'Частота ноты {note_input} составляет {frequency:.2f} Гц')
else:
    print('Введена неверная нота.')

