class ComplexNumber:
    def __init__(self, value_a, value_b):
        self.a = value_a
        self.b = value_b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return ComplexNumber(self.a - other.a, self.b - other.b)

    def __str__(self):
        return f'{self.a} + {self.b}*i'


complex_number_1 = ComplexNumber(10, 15)
complex_number_2 = ComplexNumber(2, 5)
print(f'complex_number_1 = {complex_number_1}\ncomplex_number_2 = {complex_number_2}')
print(f'Сложение двух чисел: {complex_number_1 + complex_number_2}')
print(f'Вычитание: {complex_number_1 - complex_number_2}')
