class OwnException(Exception):
    def __init__(self, msg):
        self.txt = msg


try:
    a, b = map(int, input("Введите два числа через пробел: ").split(" "))
    if b == 0:
        raise OwnException('деление на ноль запрещено')
    print(f'Реультат деления: {round(a/b, 2)}')
except ZeroDivisionError:
    print("На ноль делить нельзя")
except ValueError:
    print("Неверные значения")
except OwnException as err:
    print(err)

print("Завершение программы")
