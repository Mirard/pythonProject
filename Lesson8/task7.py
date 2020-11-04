# This Python file uses the following encoding: utf-8
class ComplexNum:
    material: float
    alleged: float

    def __init__(self, material, alleged):
        self.material = material
        self.alleged = alleged

    def __add__(self, other):
        return ComplexNum(self.material + other.material, self.alleged + other.alleged)

    def __mul__(self, other):
        return ComplexNum((self.material * other.material - self.alleged * other.alleged),
                          (self.alleged * other.material + self.material * other.alleged))

    def __str__(self):
        if self.alleged >= 0:
            return f"{self.material} + {self.alleged}i"
        else:
            return f"{self.material} - {abs(self.alleged)}i"


num1 = ComplexNum(1, 2)
num2 = ComplexNum(3, 4)
num3 = ComplexNum(-1, -5)
print("Число 1: ", num1)
print("Число 2: ", num2)
print("Число 3: ", num3)
print("Сумма числа 1 и числа 2: ", num1.__add__(num2))
print("Произедение числа 1 на число 2: ", num1.__mul__(num2))
print("Сумма числа 1 и числа 3: ", num1.__add__(num3))
print("Произедение числа 1 на число 3: ", num1.__mul__(num3))

