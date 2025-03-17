class Fraction:
    def __new__(cls, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        return super().__new__(cls)

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        common_divisor = gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    @property
    def value(self):
        return round(self.numerator / self.denominator, 3)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    @staticmethod
    def from_float(value):
        numerator = int(value * 1e3)
        denominator = 1e3
        return Fraction(numerator, denominator)

    @classmethod
    def from_string(cls, string):
        numerator, denominator = map(int, string.split('/'))
        return cls(numerator, denominator)


class FractionMatrix:
    def __new__(cls, matrix):
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise ValueError("All rows must have the same length.")
        return super().__new__(cls)

    def __init__(self, matrix):
        self.matrix = [[Fraction.from_string(str(cell)) if isinstance(cell, str) else cell for cell in row] for row in matrix]
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions.")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return FractionMatrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions.")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return FractionMatrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must equal number of rows in the second.")
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return FractionMatrix(result)

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return FractionMatrix(result)

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square.")
        if self.rows == 1:
            return self.matrix[0][0]
        if self.rows == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        det = 0
        for c in range(self.cols):
            submatrix = [row[:c] + row[c+1:] for row in self.matrix[1:]]
            submatrix = FractionMatrix(submatrix)
            det += ((-1) ** c) * self.matrix[0][c] * submatrix.determinant()
        return det

    @staticmethod
    def identity(size):
        return FractionMatrix([[Fraction(1, 1) if i == j else Fraction(0, 1) for j in range(size)] for i in range(size)])

    @classmethod
    def from_list_of_lists(cls, list_of_lists):
        return cls(list_of_lists)