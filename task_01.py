class Matrix:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.value])

    def __add__(self, other):
        new_matrix = []
        big_matrix = self.value if len(self.value) >= len(other.value) else other.value
        small_matrix = other.value if len(self.value) >= len(other.value) else self.value
        small_matrix.extend([[0, ]] * (len(big_matrix) - len(small_matrix)))
        for i, row in enumerate(big_matrix):
            new_matrix.append(
                map(sum, zip(
                    big_matrix[i] + [0, ] * (len(small_matrix[i]) - len(big_matrix[i])),
                    small_matrix[i] + [0, ] * (len(big_matrix[i]) - len(small_matrix[i]))
                ))
            )
        return Matrix(new_matrix)


matrix_1 = Matrix([[2, 3, 5], [3, 4], [10, 11]])
matrix_2 = Matrix([[1, 5], [4, 7]])

print(f'Matrix 1:\n{matrix_1}')
print(f'Matrix 2:\n{matrix_2}')
print(f'Matrix 3:\n{matrix_1 + matrix_2}')
