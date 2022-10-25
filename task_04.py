import copy

class OwnException(Exception):
    def __init__(self, msg):
        self.txt = msg


class WareHouse:
    def __init__(self):
        self.__storage_location = {
            'base': {},
            'dep_1': {},
            'dep_2': {},
            'repair': {}
        }

    def __str__(self):
        result_string = ''
        for sklad in self.__storage_location:
            result_string += f'Склад {sklad}:\n'
            if len(self.__storage_location[sklad]) == 0:
                result_string += f'Ничего нет\n'
            else:
                for equipment in self.__storage_location[sklad]:
                    if self.__storage_location[sklad][equipment].count > 0:
                        result_string += f'\t{self.__storage_location[sklad][equipment].eq_type}: ' \
                                         f'{self.__storage_location[sklad][equipment].name} ' \
                                         f'кол-во {self.__storage_location[sklad][equipment].count}\n'
        return f'Содержимое складов \n{result_string}'

    def put_on_warehouse(self, equipment, department='base'):
        self.__storage_location[department][equipment.name] = equipment

    @property
    def ware_house(self):
        return self.__storage_location

    def eq_moving(self, equipment, from_department, to_department, count):
        if self.ware_house[from_department].get(equipment.name):
            if count <= self.ware_house[from_department].get(equipment.name).count:
                new_eq = copy.deepcopy(equipment)
                new_eq.count = count
                self.put_on_warehouse(new_eq, to_department)
                self.ware_house[from_department].get(equipment.name).count = \
                    self.ware_house[from_department].get(equipment.name).count - count
            else:
                print(f'{equipment.name} недостаточное кол-во на складе {from_department}')
        else:
            print(f'{equipment.name} не найден на складе {from_department}')


class Equipment:
    def __init__(self, name, price, eq_type):
        self.eq_type = eq_type
        self.name = name
        self.__count = None
        self.price = price

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        try:
            if type(value) == 'str':
                raise OwnException('Значение не число, введите корректное значение')
            elif value < 0:
                raise  OwnException('Число не может быть отрицательным')
            else:
                self.__count = value
        except OwnException as err:
            print(f'Ошибка установки кол-ва техники: {err}')


class Printer(Equipment):
    printers_type = ['printer', 'mfps']
    connections_type = ['local', 'network']

    def __init__(self, name, price):
        super().__init__(name, price, 'Printer')
        self.__printer_type = None
        self.__connection_type = None

    @property
    def printer_type(self):
        return self.__printer_type

    @printer_type.setter
    def printer_type(self, value):
        if value not in Printer.printers_type:
            print(f'Допустимые значения {Printer.printers_type}')
        else:
            self.__printer_type = value

    @property
    def connection_type(self):
        return self.__connection_type

    @connection_type.setter
    def connection_type(self, value):
        if value not in Printer.connections_type:
            print(f'Допустимые значения {Printer.connections_type}')
        else:
            self.__connection_type = value


class Scaner(Equipment):
    max_formats = ['A4', 'A3', 'A2', 'A1', 'A0']
    connections_type = ['local', 'network']

    def __init__(self, name, price):
        super().__init__(name, price, 'Scaner')
        self.__max_format = None
        self.__connection_type = None

    @property
    def max_format(self):
        return self.__max_format

    @max_format.setter
    def max_format(self, value):
        if value not in Scaner.max_formats:
            print(f'Допустимые значения {Scaner.max_formats}')
        else:
            self.__max_format = value

    @property
    def connection_type(self):
        return self.__connection_type

    @connection_type.setter
    def connection_type(self, value):
        if value not in Scaner.connections_type:
            print(f'Допустимые значения {Scaner.connections_type}')
        else:
            self.__connection_type = value


ware_house = WareHouse()
print(ware_house)
printer_1 = Printer('printer_1', 1000)
printer_1.printers_type = 'mfps'
printer_1.connections_type = 'network'
printer_1.count = 1
ware_house.put_on_warehouse(printer_1)
printer_2 = Printer('printer_2', 3000)
printer_2.printers_type = 'local'
printer_2.connections_type = 'local'
printer_2.count = 1
ware_house.put_on_warehouse(printer_2)
scaner_1 = Scaner('scaner_1', 2300)
scaner_1.connections_type = 'local'
scaner_1.count = 2
scaner_1.max_format = 10
scaner_1.max_format = 'A3'
scaner_2 = Scaner('scaner_2', 1300)
scaner_2.connections_type = 'network'
scaner_2.count = 1
scaner_1.max_format = 'A4'
ware_house.put_on_warehouse(scaner_1, 'dep_1')
ware_house.put_on_warehouse(scaner_2)
print(ware_house)
ware_house.eq_moving(scaner_2, 'base', 'dep_2', 1)
print(f'После перемещения {ware_house}')
ware_house.eq_moving(scaner_1, 'base', 'dep_2', 1)
