# Задача 4 и 5: Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Машина поехала вперед"

    def stop(self):
        return "Машина остановилась"

    def turn(self, direction: int):
        if direction < 0:
            return "Машина повернула налево"
        else:
            return "Машина повернула направо"

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Скорость Вашего автомобиля {self.speed} км/ч, превышена норма 60 км/ч"
        else:
            return self.speed


class SportCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Скорость Вашего автомобиля {self.speed} км/ч, превышена норма 40 км/ч"
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


mess1 = "\nПроверим класс Car"
my_car1 = Car(90, "red", "BMW", False)
mess2 = "\nПроверим класс TownCar с большой скоростью"
my_car2 = TownCar(61, "black", "BMW", False)
mess3 = "\nПроверим класс TownCar с нормальной скоростью"
my_car3 = TownCar(60, "black", "Mazda", False)
mess4 = "\nПроверим класс SportCar"
my_car4 = SportCar(180, "red", "Ferrari", False)
mess5 = "\nПроверим класс WorkCar с большой скоростью"
my_car5 = WorkCar(41, "black", "Tesla", False)
mess6 = "\nПроверим класс WorkCar с нормальной скоростью"
my_car6 = WorkCar(40, "black", "Tesla", False)
mess7 = "\nПроверим класс PoliceCar"
my_car7 = PoliceCar(120, "black", "Mercedes", True)
cars = [my_car1, my_car2, my_car3, my_car4, my_car5, my_car6, my_car7]
mess = [mess1, mess2, mess3, mess4, mess5, mess6, mess7]
ind = 0

while ind < len(cars):
    print(mess[ind])
    print(type(cars[ind]))
    print(f"Характеристики автомобиля:\nСкорость: {cars[ind].speed} км/ч\nЦвет: {cars[ind].color}"
          f"\nМарка: {cars[ind].name}\nМашина полицейская? {cars[ind].is_police}")
    print(cars[ind].go())
    print(cars[ind].show_speed())
    print(cars[ind].turn(-1))
    print(cars[ind].go())
    print(cars[ind].turn(0))
    print(cars[ind].stop())
    ind += 1
