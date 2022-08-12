def int_func(tmp_str):
    return tmp_str[0].upper() + tmp_str[1:]


print(f'Полученное слово {int_func(input("Введите слово: "))}')
