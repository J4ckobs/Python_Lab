import random

class RandMatrix:
    def __init__(self, cols=3, rows=3, min_range=-20, max_range=20, List = None):
        if not List:
            self.cols = cols
            self.rows = rows
            self.min_range = min_range
            self.max_range = max_range
            self.matrix = [[self.cols*x + y+1 for y in range(self.cols)] for x in range(self.rows)]  # [random.randrange(min_range, max_range)
            # for x in range(self.cols * self.rows)]
        else:
            self.cols = cols
            self.rows = rows
            self.matrix = List

    def __str__(self):
        result = ""
        for row in self.matrix:
            for num in row:
                result += f"  {num} "
            result += "\n"
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise Exception("Dimensions of matrixes not matching for multiplying")

        result = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return RandMatrix(self.cols, other.rows, List=result)


matrix1 = RandMatrix(2, 3)

matrix2 = RandMatrix(3, 2)

print("Macierz #1\n", matrix1)

print("Macierz #2\n",matrix2)

print("Wynik mnożenia macierzy #1 i #2\n",matrix1 * matrix2)
