# This Python file uses the following encoding: utf-8
class TypeError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_array = []
user_el = ""

while user_el.lower() != "stop":
    user_el = input("Введите элемент, чтобы добавить его в список, для выхода введите stop >>> ")
    try:
        if float(user_el) != "":
            user_array.append(float(user_el))
        elif float(user_el) == "":
            user_array.append(0)
        else:
            raise TypeError(f"Элемент {user_el} невозможно конвертировать в число")
    except ValueError:
        print(f"Элемент {user_el} невозможно конвертировать в число")
    except TypeError as err:
        print(err)

print("Список введенных чисел: ", user_array)
