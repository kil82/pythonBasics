def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Exception! Division by zero')
        return


a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
print(f'Результат деления {a}/{b}={division(a, b)}')
