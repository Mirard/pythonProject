class Stationery:
    title: str

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        return "Пишем ручкой"


class Pencil(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        return "Рисуем карандашом"


class Handle(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        return "Закрашиваем маркером"


my_tool1 = Stationery("Кисточка")
print(my_tool1.draw())
my_tool2 = Pen("Ручка")
print(my_tool2.draw())
my_tool3 = Pencil("Карандаш")
print(my_tool3.draw())
my_tool4 = Handle("Маркер")
print(my_tool4.draw())
