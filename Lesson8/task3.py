# This Python file uses the following encoding: utf-8
class _ValueError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_array = []
user_el = ""

while user_el.lower() != "stop":
    user_el = input("Введите элемент, чтобы добавить его в список, для выхода введите stop >>> ")
    try:
        if user_el.isdecimal():
            if float(user_el) == "":
                user_array.append(0)
            else:
                user_array.append(float(user_el))
        else:
            raise ValueError(f"Элемент {user_el} невозможно конвертировать в число")
    except ValueError as err:
        print(err)

print("Список введенных чисел: ", user_array)
