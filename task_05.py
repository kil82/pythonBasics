sum_value = 0


def my_func(values_list):
    global sum_value
    values_list = [float(value) for value in values_list]
    sum_value += sum(values_list)
    return sum_value


while True:
    tmp_value = input('Введите числа через пробел, для завершения ввода используйте сивол q: ').split(' ')
    if tmp_value[-1].upper() == 'Q':
        my_func(tmp_value[0:-1])
        break
    else:
        my_func(tmp_value)
print(f'сумма всех введенных чиел {sum_value}')
