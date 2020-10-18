class Worker:
    name: str
    surname: str
    position: str
    wage: float
    bonus: float
    _income: {}

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        super().__init__(name, surname, position, wage, bonus)
        self._income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"Доход сотрудника с учетом вычета налога: {(self.wage + self.bonus) * 0.87}"


check_position = Position("Иван", "Иванов", "обычный сотрудник", 12400, 600)
print(check_position.get_full_name())
print(check_position.get_total_income())
