import time


class TrafficLight:
    __color = {7: 'red', 2: 'yellow', 5: 'green'}

    def __init__(self):
        print(f'Светофор инициализирован цвет {self.__color[7]}')

    def running(self):
        print(f'Светофор запущен')
        while True:
            for key in self.__color.keys():
                print(f'Цвет: {self.__color[key]}')
                time.sleep(key)


traffic_light = TrafficLight()
traffic_light.running()
