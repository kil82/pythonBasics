profit = int(input('Введите прибыль фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if profit < 0 or profit < costs:
    print('Фирма работает в убыток')
elif profit > costs:
    person_count = int(input('Введите кол-во человек в фиреме: '))
    rent = (profit/costs)*100
    person_profit = profit/person_count
    print(f'Фирма работает в прибыль. Рентабельность выручки {rent:.2f}%. Прибыль на сотрудника {person_profit:.2f}')
elif profit == costs:
    print('Баланс фирмы нулевой')
