with open('task_05.txt', 'w+') as f_obj:
    f_obj.write(input('введите числа разделенные пробелом: '))
    f_obj.seek(0)
    content = f_obj.read()
print(f"Сумма введенных чисел равна: {sum([float(item) for item in content.split(' ')])}")
