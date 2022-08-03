a = int(input('Введите a: '))
b = int(input('Введите b: '))

day_counter = 1
while a < b:
    a += a * 0.1
    day_counter += 1
print(f'Спортсмен достиг конечного результата на {day_counter} день')
