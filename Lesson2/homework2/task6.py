name = []
price = []
quantity = []
measure = []

product_struct = []
index = 1

user_string = input(f"Введите название товара №{index}, для выхода из заполнения введите exit >>> ")
while user_string.lower() != "exit":
    while len(user_string) == 0 or len(user_string) == user_string.count(" "):
        print("\nЗначение не должно быть пустым. Введите новое значение или exit для выхода")
        user_string = input(f"Введите название товара №{index}, для выхода из заполнения введите exit >>> ")
    if user_string != "exit":
        name.append(user_string)
    else:
        print("Спасибо за использование нашей программы!")
        break
    user_string = input(f"Введите цену товара №{index}, для выхода из заполнения введите exit >>> ")
    while len(user_string) == 0 or len(user_string) == user_string.count(" "):
        print("\nЗначение не должно быть пустым. Введите новое значение или exit для выхода")
        user_string = input(f"Введите цену товара №{index}, для выхода из заполнения введите exit >>> ")
    if user_string != "exit":
        try:
            price.append(float(user_string))
        except ValueError:
            print(f"Вы ввели не число! Установлено значение по умолчанию 0")
            price.append(0)
    else:
        print("Спасибо за использование нашей программы!")
        break
    user_string = input(f"Введите количество товара №{index}, для выхода из заполнения введите exit >>> ")
    while len(user_string) == 0 or len(user_string) == user_string.count(" "):
        print("\nЗначение не должно быть пустым. Введите новое значение или exit для выхода")
        user_string = input(f"Введите количество товара №{index}, для выхода введите exit >>> ")
    if user_string != "exit":
        try:
            quantity.append(int(user_string))
        except ValueError:
            print(f"Вы ввели не число! Установлено значение по умолчанию 0")
            quantity.append(0)
    else:
        print("Спасибо за использование нашей программы!")
        break
    user_string = input(f"Введите единицы измерения товара №{index}, для выхода из заполнения введите exit >>> ")
    while len(user_string) == 0 or len(user_string) == user_string.count(" "):
        print("\nЗначение не должно быть пустым. Введите новое значение или exit для выхода")
        user_string = input(f"Введите единицы измерения товара №{index}, для выхода из заполнения введите exit >>> ")
    if user_string != "exit":
        measure.append(user_string)
    else:
        print("Спасибо за использование нашей программы!")
        break
    product_struct.append(
        (index, {"название": name[index - 1], "цена": price[index - 1], "количество": quantity[index - 1],
                 "eд": measure[index - 1]}))
    index = index + 1
    user_string = input(f"Введите название товара №{index}, для выхода из заполнения введите exit >>> ")

print("\n\nСтруктура продуктов: ")
for elem in product_struct:
    print("\n", elem)

analytic = {"название": name, "цена": price, "количество": quantity,
            "eд": measure}
print("\n\nАналитика о товарах: ")
for elem in analytic.items():
    print("\n", elem)
