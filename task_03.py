class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def get_income(self):
        return self._income


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Фамилия Имя: {self.surname} {self.name}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {sum(self.get_income().values())}')


worker_1 = Position('Ivan', 'Ivanov', 'manager', 10000, 5000)
worker_2 = Position('Alex', 'Sergeev', 'manager', 12000, 9000)
worker_1.get_full_name()
worker_1.get_total_income()
worker_2.get_full_name()
worker_2.get_total_income()
