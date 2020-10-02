num_list = [7, 5, 3, 3, 2]
print("Ваш список: ", num_list)
user_num = input("Введите целое число, чтобы добавить его в список, для выхода введите exit >>> ")
while user_num != "exit":
    index = 0
    try:
        new_num = int(user_num)
        count = num_list.count(new_num)
        # Проверяем, есть ли уже такое число
        if count != 0:
            num_index = num_list.index(new_num)
            num_list.insert(count + num_index, new_num)
        # Если нет - проверяем с 1м и последним значением, а уж потом делаем обход
        else:
            if num_list[index] < new_num:
                num_list.insert(index, new_num)
            elif num_list[len(num_list) - 1] >= new_num:
                num_list.append(new_num)
            else:
                index = 0
                flag = 0
                while index < (len(num_list)) and flag == 0:
                    if num_list[index] >= new_num > num_list[index + 1]:
                        num_list.insert(index + 1, new_num)
                        flag = 1
                    index = index + 1
        print("Ваш новый список: ", num_list)
    except ValueError:
        print(f"Вы ввели не число!")
        print("Ваш список: ", num_list)
    user_num = input("Введите целое число, чтобы добавить его в список, для выхода введите exit >>> ")
print("\nВаш итоговый список: ", num_list)
