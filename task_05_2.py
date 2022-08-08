task_list = [7, 5, 3, 3, 2]
while True:
    rating = int(input('Введите рэйтинг: '))
    if rating <= task_list[len(task_list) - 1]:
        task_list.append(rating)
    else:
        for i, el in enumerate(task_list):
            if el < rating:
                task_list.insert(i, rating)
                break
    if input('Закончить введение рэйтингов Yy/Nn (N)? ').capitalize() == 'Y':
        break
print(f'полученный список рэйтингов {task_list}')
