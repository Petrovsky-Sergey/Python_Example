# получить от пользователя количество секунд
total_seconds = float(input('Введите количество секунд: '))

# получить количество часов
hours = total_seconds // 3600

# получить количество оставшихся минут
minutes = (total_seconds // 60) % 60

# получить количество оставшихся секунд
seconds = total_seconds % 60

# показать результаты
print('Вот время в часах, минутах, секундах:')
print('Часы:', hours)
print('Минуты:', minutes)
print('Секунды', seconds)
