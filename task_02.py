user_input = int(input('Введите время в секундах: '))

hours = user_input//3600
user_input -= hours * 3600
seconds = user_input % 60
minutes = user_input // 60
print(f'Время {hours:0>2}:{minutes:0>2}:{seconds:0>2}')
