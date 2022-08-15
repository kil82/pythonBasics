from functools import reduce


def calc(a, b):
    return a * b


print(f'произведение всех элементов {reduce(calc, [item for item in range(99, 1001) if item % 2 == 0])}')
