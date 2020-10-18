class Road:
    _length: float
    _width: float

    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def calculate(self, weight: float, depth: float):
        return self._length * self._width * weight * depth


user_length = input("Введите длину пути в метрах >>> ")
user_width = input("Введите ширину пути в метрах >>> ")
user_weight = input("Введите массу асфальта в кг на 1 кв.см. >>> ")
user_depth = input("Введите толщину дороги в см >>> ")
user_nums = [user_length, user_width, user_weight, user_depth]
user_nums_name = ["Длина", "Ширина", "Масса", "Толщина"]
ind = 0

while ind < len(user_nums):
    try:
        user_nums[ind] = abs(float(user_nums[ind]))
    except ValueError:
        print(f"{user_nums_name[ind]} не является числом, установлено значение по умолчанию: 1")
        user_nums[ind] = 1
    ind += 1

user_road = Road(user_nums[0], user_nums[1])
print(
    f"Для покрытия дороги длиной {user_nums[0]} м, шириной {user_nums[1]} м, "
    f"массой асфальта на 1 кв.см. {user_nums[2]}, толщиной {user_nums[3]} см, "
    f"Вам понадобится {user_road.calculate(user_nums[2], user_nums[3])} т асфальта")
