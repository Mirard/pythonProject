user_string = input("Введите слова через пробел: ")

user_list = list(user_string)
list_len = len(user_list)
index = 0

if list_len == 0:
    print("Вы не ввели значение, разбиение строк невозможно")
    index = 1
else:
    count = 0
    main_count = user_string.count(" ")
    while count <= main_count and len(user_string) != 0:
        try:
            space_ind = user_string.index(" ")
            if user_string[0] == " ":
                index = index - 1
            elif 0 < space_ind < 10:
                print(f"Строка №{index + 1}: ", user_string[0:space_ind])
            else:
                print(f"Строка №{index + 1}: ", user_string[0:10])
            user_string = user_string[(space_ind + 1):]
        except ValueError:
            print(f"Строка №{index + 1}: ", user_string[0:10])
        count = count + 1
        index = index + 1

if index == 0:
    print("Ваша строка состояла только из пробелов")
