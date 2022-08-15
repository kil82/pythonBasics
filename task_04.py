task_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Исходный список {task_list}')
print(f'Список уникальных элементов {[item for item in task_list if task_list.count(item) == 1]}')
