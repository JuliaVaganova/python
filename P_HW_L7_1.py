# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

from itertools import zip_longest


class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        a = ("\n".join((str(row)).replace(",", " ") for row in self.matrix_data)).replace("]", "").replace("[", "")
        return f"Сумма матриц: \n{a}"

    def __add__(self, other):
        new_matrix = []
        for x in range(abs(len(self.matrix_data) - len(other.matrix_data))):
            if len(self.matrix_data) > len(other.matrix_data):
                other.matrix_data.append([0])
            else:
                self.matrix_data.append([0])
        for i in range(max(len(self.matrix_data), len(other.matrix_data))):
            new_matrix.append([x + y for x, y in zip_longest(self.matrix_data[i], other.matrix_data[i], fillvalue=0)])
        return Matrix(new_matrix)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_3 = Matrix([[10, 10, 10], [10, 10, 10], [10, 10, 10]])

print(matrix_1 + matrix_2 + matrix_3)
