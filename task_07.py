def int_func(tmp_str):
    tmp_str = [word[0].upper() + word[1:] for word in tmp_str.split()]
    return " ".join(tmp_str)


print(f'Строка после обработки {int_func(input("Введите слова через пробел: "))}')
