def print_person(first_name, second_name, birth_year, city, email, phone_number):
    print(f'Имя: {first_name}; Фамилия: {second_name}; Год рождения: {birth_year}; E-mail: {email}; '
          f'Номер телефона: {phone_number}; Город проживания: {city};')


f_name = input('Введите имя: ')
s_name = input('Введите фамилию: ')
b_year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите e-mail: ')
phone = input('Введите номер телефона: ')
print_person(first_name = f_name, second_name = s_name, city = city, birth_year = b_year, phone_number = phone, email = email)
