class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановлена')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self, current_speed):
        print(f'Текущая скорость машины {self.name} - {current_speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self, current_speed):
        if int(current_speed) > 60:
            print(f'Скорость машины {self.name} превышена')
        else:
            print(f'Текущая скорость машины {self.name} - {current_speed}')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self, current_speed):
        if int(current_speed) > 40:
            print(f'Скорость машины {self.name} превышена')
        else:
            print(f'Текущая скорость машины {self.name} - {current_speed}')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town_car = TownCar(80, 'black', 'car1')
work_car = WorkCar(70, 'white', 'car2')
sport_car = SportCar(150, 'red', 'car3')
police_car = PoliceCar(200, 'black', 'car4')

town_car.go()
town_car.turn('влево')
town_car.show_speed(65)
town_car.stop()

work_car.go()
work_car.turn('вправо')
work_car.show_speed(30)
work_car.stop()

sport_car.go()
sport_car.turn('влево')
sport_car.show_speed(100)
sport_car.stop()

police_car.go()
police_car.turn('влево')
police_car.show_speed(25)
police_car.stop()
