user_input = input('Введите любое число: ')

double_value = user_input + user_input
tripple_value = double_value + user_input
itog = int(user_input) + int(double_value) + int(tripple_value)
print(f'Сумма числе {user_input}+{double_value}+{tripple_value} = {itog}')
