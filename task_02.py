task_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [task_list[i + 1] for i in range(0, len(task_list) - 1) if task_list[i + 1] > task_list[i]]

print(f'Исходный список {task_list}')
print(f'Сгенерированный список {new_list}')
