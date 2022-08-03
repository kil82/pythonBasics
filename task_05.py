profit = int(input('Введите прибыль фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if profit < 0 or profit < costs:
    print('Фирма работает в убыток')
elif profit > costs:
    print('Фирма работает в прибыль')
elif profit == costs:
    print('Баланс фирмы нулевой')
