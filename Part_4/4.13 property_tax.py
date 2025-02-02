# Эта программа показывает налоги на имущество

TAX_FACTOR = 0.0065  # Представляет налоговый коэффициент

# Получить номер первого лота
print('Введите номер имущественного лота либо 0 для завершения. ')
lot = int(input('Номер лота: '))

# Продолжить обработку пока пользователь
# не введет номер лота 0
while lot != 0:
    # Получить стоимость имущества
    value = float(input('Введите стоимость имущества: '))

    # Исчислить налог на имущества
    tax = value * TAX_FACTOR

    # Показать налог
    print(f'Налог на имущество: ${tax:.2f}')

    # Получить следующий номер лота
    print('Введите следующий номер либо 0, чтобы завершить')
    lot = int(input('Номер лота: '))