def my_func(value_x, value_y):
    x = 1
    for i in range(0, value_y, -1):
        x *= value_x
    return 1 / x, value_x ** value_y


x = float(input('введите х (значение больше 0): '))
y = int(input('введите y (целое меньше 0): '))

if x <= 0 or y > -1:
    print('Неверный ввод')
else:
    value_1, value_2 = my_func(x, y)
    print(f'Результат возведения {x} в степень {y} по циклу = {value_1}, с использованием ** = {value_2}')
