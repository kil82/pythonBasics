user_str = input('Введите слова через пробел: ')
string_list = user_str.split(' ')
for i, el in enumerate(string_list):
    print(f'{i + 1} {el[:10]}')
