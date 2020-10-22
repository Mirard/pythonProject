class Matrix:
    values: list

    def __init__(self, values: list):
        self.values = values

    def __add__(self, other):
        new_matrix = []
        ind1 = 0
        while ind1 < len(self.values):
            ind2 = 0
            part_matrix = []
            while ind2 < len(self.values[ind1]):
                part_matrix.append(self.values[ind1][ind2] + other.values[ind1][ind2])
                ind2 += 1
            new_matrix.append(part_matrix)
            ind1 += 1
        return new_matrix

    def __str__(self):
        return f"{self.values}"


my_matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
my_matrix2 = Matrix([[2.5, 3], [4, 5], [-5, -7]])
print("Первая матрица: ", my_matrix1.__str__())
print("Вторая матрица: ", my_matrix2.__str__())
print("Сумма матриц: ", my_matrix1 + my_matrix2)
