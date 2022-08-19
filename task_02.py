with open('task_02.txt') as f_obj:
    word_count = 0
    line_count = 0
    for line in f_obj:
        line_count += 1
        word_count = len(line.split(' '))
        print(f'Кол-во слов в строке {line_count} - {word_count}')

print(f'всего строк {line_count}')
