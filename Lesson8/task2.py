# This Python file uses the following encoding: utf-8
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class __ZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


num1 = input("Введите делимое: ")
num2 = input("Введите делитель: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    if num1 < 0 or num1 < 0:
        raise OwnError("Вы ввели отрицательное число!")
    if num2 == 0:
        raise ZeroDivisionError("Деление на 0 запрещено!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {num1/num2}")
