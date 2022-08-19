final_dict = {}
with open('task_06.txt') as f_obj:
    for line in f_obj:
        split_line = line.replace('\n', '').replace(':', '').replace('—', '').replace('(л)', '').replace('(пр)', '')\
            .replace('(лаб)', '').split(' ')
        final_dict[split_line[0]] = sum([float(item) for item in split_line[1:] if item != ''])
print(final_dict)
