task_list = [7, 5, 3, 3, 2]
while True:
    task_list.append(int(input('Введите рэйтинг: ')))
    task_list.sort(reverse = True)
    if input('Закончить введение рэйтингов Yy/Nn (N)? ').capitalize() == 'Y':
        break
print(f'полученный список рэйтингов {task_list}')
