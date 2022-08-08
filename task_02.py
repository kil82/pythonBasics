task_list = []
while True:
    task_list.append(input('введите элемент списка '))
    if input('Закончить формирования списка Yy/Nn (N)? ').capitalize() == 'Y':
        break
print(f'Заданный список {task_list}')
for i, el in enumerate(task_list):
    if i < len(task_list) - 1 and i % 2 == 0:
        tmp_value = task_list[i]
        task_list[i] = task_list[i + 1]
        task_list[i + 1] = tmp_value
print(f'Сформированный список {task_list}')
