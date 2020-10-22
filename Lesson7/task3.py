class Cell:
    def __init__(self, num: int):
        self.num = num

    def make_order(self, num: int):
        ind = 1
        cell_string = ""
        if num != "\nНевозможно выполнить вычитание: уменьшаемое число меньше вычитаемого":
            if num != "\nНевозможно выполнить деление клеток, делитель равен 0":
                if num != 0:
                    while ind <= num:
                        if ind % 5 != 0:
                            cell_string = cell_string + "*"
                        else:
                            cell_string = cell_string + "*\n"
                        ind += 1
        return cell_string

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num >= other.num:
            return self.num - other.num
        else:
            return "\nНевозможно выполнить вычитание: уменьшаемое число меньше вычитаемого"

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        if other.num == 0:
            return "\nНевозможно выполнить деление клеток, делитель равен 0"
        else:
            return self.num // other.num


cell1 = Cell(8)
cell2 = Cell(6)
cell3 = Cell(9)
cell4 = Cell(0)
print(f"Складываем {cell1.num} и {cell2.num}: ", cell1 + cell2)
print(Cell(cell1 + cell2).make_order(cell1 + cell2))
print(f"Вычитаем {cell1.num} и {cell2.num}: ", cell1 - cell2)
print(Cell(cell1 - cell2).make_order(cell1 - cell2))
print(f"Вычитаем {cell1.num} и {cell1.num}: ", cell1 - cell1)
print(Cell(cell1 - cell1).make_order(cell1 - cell1))
print(f"Вычитаем {cell1.num} и {cell3.num}: ", cell1 - cell3)
print(Cell(cell1 - cell3).make_order(cell1 - cell3))
print(f"Умножаем {cell1.num} на {cell2.num}: ", cell1 * cell2)
print(Cell(cell1 * cell2).make_order(cell1 * cell2))
print(f"Делим {cell1.num} на {cell2.num}: ", cell1 / cell2)
print(Cell(cell1 / cell2).make_order(cell1 / cell2))
print(f"Делим {cell1.num} на {cell4.num}: ", cell1 / cell4)
print(Cell(cell1 / cell4).make_order(cell1 / cell4))
