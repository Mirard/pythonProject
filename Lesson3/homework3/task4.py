user_step = input("Введите основание степени >>> ")
user_pokaz = input("Введите показатель степени >>> ")


def my_func(step, pokaz):
    try:
        step = float(step)
        pokaz = int(pokaz)
        if step == 0:
            return 0
        elif pokaz == 0:
            return 1
        elif pokaz > 0:
            print(
                "Эта программа для вычисления степени с отрицательным показателем! Вернется значение по умолчанию - 0")
            return 0
        else:
            index = 0
            result = 1
            while index < abs(pokaz):
                result = result * (1 / step)
                index = index + 1
            return result
    except ValueError:
        print(f"Не все значения являются числами, вернется значение по умолчанию - 0")
        return 0


print("Результат возведения в отрицательную степень: ", my_func(user_step, user_pokaz))
