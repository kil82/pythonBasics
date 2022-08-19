with open("task_01.txt", 'w+') as f_obj:
    while True:
        user_str = input("Введите строку, пустая строка окончания ввода: ")
        if user_str == "":
            f_obj.seek(0)
            print(f_obj.read())
            break
        f_obj.write(user_str + "\n")
