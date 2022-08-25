class Road:
    _length = 0
    _width = 0
    __weight_asphalt = 25
    __height_road = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self):
        print(f'{self._width} м * {self._length} м * {self.__weight_asphalt} кг * {self.__height_road} см = '
              f'{round((self._width * self._length * self.__weight_asphalt * self.__height_road)/1000)} т')


road = Road(5000, 20)
road.calculate()
