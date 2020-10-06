# Функция разбиения строки
def prepare_list(string):
    user_list = list(string)
    list_len = len(user_list)
    index = 0
    result_list = []
    if list_len == 0:
        print("\nВы не ввели значение, сумма элементов будет равна 0")
        index = index + 1
    else:
        count = 0
        main_count = string.count(" ")
        while count <= main_count and len(string) != 0:
            try:
                space_ind = string.index(" ")
                if string[0] == " ":
                    index = index - 1
                else:
                    result_list.append(string[0:space_ind])
                string = string[(space_ind + 1):]
            except ValueError:
                result_list.append(string[0:])
            count = count + 1
            index = index + 1

    if index == 0:
        print("\nВаша строка состояла только из пробелов")
    else:
        print("\nОбрабатываем Вашу строку...")
    return result_list


# Функция подсчета суммы элементов
def find_sum(int_list):
    char_flag = 0
    list_index = 0
    sum_result = 0
    while list_index < len(int_list):
        try:
            current_element = float(int_list[list_index])
            sum_result = sum_result + current_element
        except ValueError:
            char_flag = 1
        list_index = list_index + 1

    return sum_result, char_flag


# Тело программы
flag = 0
result_list_sum = 0
while flag == 0:
    user_string = input("\nВведите числа через пробел: ")
    list_sum, flag = find_sum(prepare_list(user_string))
    result_list_sum = result_list_sum + list_sum
    print("Сумма числовых элементов введенной строки: ", result_list_sum)
