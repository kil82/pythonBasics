from itertools import count, cycle

task_list = []
new_list = []
i = 0
for el in count(10):
    task_list.append(el)
    if el > 20:
        break
for el in cycle(task_list):
    new_list.append(el)
    if i > 30:
        break
    i += 1
print(f'Сгенерированный список {task_list}')
print(f'Список с повторениями {new_list}')
