task_list = [1, True, 'str', 9.85, complex(4, 2), (1, 2, 3), None, [4, 5, 6], {7, 8, 9}, {'1': 2, '2': 3}, b'text',
             bytearray(b'text_bytes_array')]
for el in task_list:
    print(f'Type of elemnet {el} is {type(el)}')
