from functools import reduce


def fact(n):
    for i in range(1, n + 1, 1):
        yield i


def my_func(a, b):
    return int(a) * int(b)


fact_counter = int(input('Введите n: '))
fact_list = []
for el in fact(fact_counter):
    fact_list.append(str(el))
print(f'Факториал числа {fact_counter} = {" * ".join(fact_list)} = {reduce(my_func, fact_list)}')
