import json
firm_list = []
firm_dict = {}
average_dict = {'average_profit': 0}
count_profit = 0
with open('task_07.txt') as f_obj:
    for line in f_obj:
        split_line = line.replace('\n', '').split(' ')
        firm_dict[split_line[0]] = float(split_line[2]) - float(split_line[3])
        if float(split_line[2]) - float(split_line[3]) > 0:
            count_profit += 1
average_dict['average_profit'] = round(sum([item for item in firm_dict.values() if item > 0])/count_profit, 2)
firm_list.append(firm_dict)
firm_list.append(average_dict)
with open('task_07.json', 'w') as f_json:
    json.dump(firm_list, f_json)
