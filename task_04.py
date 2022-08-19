change_dict = {'1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь'}
new_line_symb = '\n'
with open('task_04_final.txt', 'w') as f_wr_obj:
    with open('task_04.txt') as f_r_obj:
        for line in f_r_obj:
            split_line = line.replace('\n', '').split(' — ')
            if change_dict.get(split_line[1]):
                f_wr_obj.write(f"{change_dict.get(split_line[1])} — {split_line[1]}{new_line_symb}")
