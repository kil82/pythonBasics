from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calced_material(self):
        pass


class Coat(Clothes):

    def __init__(self, name, size: float):
        super(Coat, self).__init__(name)
        self.size = size

    @property
    def calced_material(self):
        return f'{self.name} calculated material {round(self.size / 6.5 + 0.5, 2)}'


class Suit(Clothes):

    def __init__(self, name, height: float):
        super(Suit, self).__init__(name)
        self.height = height

    @property
    def calced_material(self):
        return f'{self.name} calculated material {round((self.height / 100) * 2 + 0.3, 2)}'


coat = Coat("Coat 1", 20)
print(coat.calced_material)

suit = Suit("Suit 1", 180)
print(suit.calced_material)
