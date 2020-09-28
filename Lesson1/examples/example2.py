# password = input("Введите пароль >>> ")
#
# original_password = "correct"
#
# if original_password == password:
#     print("The password is correct")
# else:
#     print("The password is incorrect")

age = int(input("Введите возраст >>> "))

if age >= 14:
    if 20 <= age < 45:
        print("можете поменять паспорт")
    else:
        print("можете получить паспорт")
elif age < 0:
    print("возраст должен быть более 0")
else:
    print("нельзя получить паспорт")
