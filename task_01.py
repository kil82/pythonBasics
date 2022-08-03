a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
operation = input('Введите обозначение операции (+,-,*,/): ')

if operation == '+':
    print(f'Сумма {a}+{b}={a+b}')
elif operation == '-':
    print(f'Разность {a}-{b}={a-b}')
elif operation == '*':
    print(f'Произведение {a}*{b}={a*b}')
elif operation == '/':
    print(f'Деление {a}/{b}={a/b}')
else:
    print(f'Введенная операция {operation} не распознана')
    