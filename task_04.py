str_user_input = input('Введите целое положительное число: ')

user_input = int(str_user_input)
max_digit = 0
while True:
    new_digit = user_input % 10
    if new_digit == 9:
        max_digit = new_digit
        break
    elif new_digit > max_digit:
        max_digit = new_digit
    elif user_input == 0:
        break
    user_input //= 10
print(f'максимальная цифра в числе {str_user_input} - {max_digit}')
