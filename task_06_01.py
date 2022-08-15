from sys import argv

try:
    start_count = int(argv[1])
    print(f'Целые числа от {start_count} до {start_count + 10}: {[i for i in range(start_count, start_count + 10, 1)]}')
except Exception as ex:
    print(f'Ошибка запуска скрипта {ex}, пример использования python task_06_01.py 3')

