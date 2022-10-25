class Data:
    __year = 0
    __month = 0
    __day = 0
    __data = ''

    def __init__(self, value: str):
        self.__data = value

    @classmethod
    def data_to_int(cls, value):
        cls.__day, cls.__month, cls.__year = map(int, value.split('-'))
        return f'День {cls.__day}, месяц {cls.__month}, год {cls.__year}, тип дня {type(cls.__day)}, ' \
               f'тип месяца {type(cls.__month)}, тип года {type(cls.__year)}'

    @staticmethod
    def check_values(day, month, year):
        result_string = ""
        if 0 < day < 32:
            result_string += 'Корректный день, '
        else:
            result_string += 'Некорректный день, '
        if 0 < month < 13:
            result_string += 'Корректный месяц, '
        else:
            result_string += 'Некорректный месяц, '
        if 0 < year:
            result_string += 'Корректный год, '
        else:
            result_string += 'Некорректный год, '
        return result_string


data = input('введите дату в формате день-месяц-год: ')
print(f'Разложенная дата {Data.data_to_int(data)}')
day, month, year = map(int, data.split('-'))
print(f"Проверка значений {Data.check_values(day, month, year)}")
