from abc import ABC, abstractmethod


class MyClothes(ABC):
    @abstractmethod
    def __init__(self, my_type: str, name: str, size: float):
        self.my_type = my_type
        self.name = name
        self.size = size


class Clothes(MyClothes):

    def __init__(self, my_type: str, name: str, size: float):
        self.name = name
        self.size = size
        self.my_type = my_type

    @property
    def calc(self):
        if self.my_type == "Coat":
            return self.size / 6.5 + 0.5
        elif self.my_type == "Suit":
            return self.size * 2 + 0.3
        else:
            print("Такая одежда не производится")
            return 0


c1 = Clothes("Coat", "MyCoat", 6.5)
c2 = Clothes("Suit", "MySuit", 1)
c3 = Clothes("Random", "MyRand", 1)
print("Проверяем пальто: ", c1.calc)
print("Проверяем костюм: ", c2.calc)
print("Проверяем одежду не из списка: ", c3.calc)
print("Общий расход ткани: ", c1.calc + c2.calc + c3.calc)
