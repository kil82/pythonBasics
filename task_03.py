class OwnException(Exception):
    def __init__(self, msg):
        self.txt = msg


input_list = []
while True:
    try:
        user_input = input('Введите элемент списка: ')
        if user_input.upper() == 'STOP':
            print(f'Список введенных значений: {input_list}')
            break
        if user_input.isdigit():
            input_list.append(float(user_input))
        else:
            raise OwnException('Введено некорректное значение, допустимы только числа')
    except OwnException as ex:
        print(ex)
        