def my_func(num1, num2, num3):
    try:
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)
        num_list = [num1, num2, num3]
        num_list.sort()
        return num_list[1] + num_list[2]
    except ValueError:
        print(f"Не все значения являются числами, вернется значение по умолчанию - 0")
        return 0


user_num1 = input("Введите число №1 >>> ")
user_num2 = input("Введите число №2 >>> ")
user_num3 = input("Введите число №3 >>> ")
print(my_func(user_num1, user_num2, user_num3))
