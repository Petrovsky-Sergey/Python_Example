# Эта программа определяет, удовлетворяет ли
# клиент требованиям банка на получение ссуды

MIN_SALARY = 30000  # Минимально допустимая годовая зарплата
MIN_YEARS = 2       # Минимально допустимый стаж
                    # на текущем месте работы
# Получить размер годовой заработанной платы клиента
salary = float(input('Введите свой годовой доход: '))

# Получить количество лет на текущем месте работы
years_on_job = int(input('Введите количество лет рабочего стажа: '))

# Определить, удовлетворяет ли клиент требованиям
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('Ваша ссуда одобрена')
    else:
        print(f'Вы должны отработать не менее {MIN_YEARS} лет, чтобы получить одобрение')
else:
    print(f'Вы должны зарабатывать не менее ${MIN_SALARY} в год, чтобы получить одобрение!')