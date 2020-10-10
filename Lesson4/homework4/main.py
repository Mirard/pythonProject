import sys
from Lesson4.homework4 import task1
# Задание 1 Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
# Не забудьте добавить их через edit
try:
    file, hours, salary, bonus = sys.argv
except ValueError:
    print("Проблема с передачей аргументов")
    exit()
try:
    print(task1.calculate(float(hours), float(salary), float(bonus)))
except ValueError:
    print("Не все аргументы являются числами")
