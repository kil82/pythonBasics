with open('task_03.txt') as f_obj:
    content = f_obj.read().split('\n')
total_sum = sum([float(item.split(' ')[1]) for item in content if item.find(' ')])
for item in content:
    if float(item.split(' ')[1]) < 20000:
        print(f"Сотрудник с зарплатой меньше 20000: {item}")
print(f'средняя величина зарплаты сотрудников {round(total_sum/len(content), 2)}')
