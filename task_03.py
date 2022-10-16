class Cell:

    def __init__(self, value: int):
        self.cell_numbers = value

    def __add__(self, other):
        return Cell(self.cell_numbers + other.cell_numbers)

    def __mul__(self, other):
        return Cell(self.cell_numbers * other.cell_numbers)

    def __truediv__(self, other):
        return Cell(self.cell_numbers / other.cell_numbers)

    def __sub__(self, other):
        if self.cell_numbers - other.cell_numbers > 0:
            return Cell(self.cell_numbers - other.cell_numbers)
        else:
            return "Can't substract this cells"

    def make_order(self, count: int):
        cell_str = '*' * self.cell_numbers
        return '\n'.join(cell_str[i:i + count] for i in range(0, len(cell_str), count))

    def __str__(self):
        return f'Result cell size {self.cell_numbers}'


cell_1 = Cell(10)
cell_2 = Cell(5)

print(cell_2 - cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(f'Make order:\n{cell_1.make_order(3)}')
