def my_func(a, b, c):
    if a > c and b > c:
        return a + b
    elif b > a and c > a:
        return b + c
    else:
        return c + a


value_1 = input('введите значение а: ')
value_2 = input('введите значение b: ')
value_3 = input('введите значение c: ')

print(f'сумма наибольших чисел: {my_func(float(value_1), float(value_2), float(value_3))}')
