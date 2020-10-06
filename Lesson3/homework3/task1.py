user_num1 = input("Введите делимое >>> ")
user_num2 = input("Введите делитель >>> ")


def delenie(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if num2 == 0:
            print("Делить на 0 нельзя =( Результат по умолчанию - 0")
            return 0
        else:
            return num1 / num2
    except ValueError:
        print(f"Вы ввели не число! Результат по умолчанию - 0")
        return 0


print(f"Результат деления числа {user_num1} на число {user_num2}: ", delenie(user_num1, user_num2))
