# Функция замены первого элемента слова
def first_char(word):
    char_list = list(word)
    not_lat = 0
    for char in char_list:
        if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
            not_lat = 1
    isint_flag = 0
    if len(word) == 0:
        isint_flag = 1
        return word, isint_flag
    else:
        new_first_elem = word[0]
        try:
            new_first_elem = int(new_first_elem)
            isint_flag = 1
        except AttributeError:
            if not_lat != 1:
                word = replace_char(new_first_elem, word)
            else:
                isint_flag = 1
                return word, isint_flag
        except TypeError:
            if not_lat != 1:
                word = replace_char(new_first_elem, word)
            else:
                isint_flag = 1
                return word, isint_flag
        except ValueError:
            if not_lat != 1:
                word = replace_char(new_first_elem, word)
            else:
                isint_flag = 1
                return word, isint_flag
        return word, isint_flag


# Функция фактической замены 1й буквы на значение в верхем регистре и возврата результата в виде строки
def replace_char(f_char, full_word):
    full_word = list(full_word)
    full_word.remove(f_char)
    f_char = f_char.upper()
    full_word.insert(0, f_char)
    new_word = ''
    index = 0
    while index < len(full_word):
        new_word = new_word + full_word[index]
        index = index + 1
    return new_word


# Функция разбиения строки с последующей заменой 1го элемента каждого слова
def prepare_list(string):
    user_list = list(string)
    list_len = len(user_list)
    res_flag = 0
    index = 0
    result_string = ''
    if list_len == 0:
        print("\nВы не ввели значение, вернется пустая строка")
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
                    npermanent_string, isint_flag = first_char(string[0:space_ind])
                    if isint_flag != 0:
                        res_flag = res_flag + 1
                    result_string = result_string + npermanent_string + ' '
                string = string[(space_ind + 1):]
            except ValueError:
                npermanent_string, isint_flag = first_char(string[0:])
                if isint_flag != 0:
                    res_flag = res_flag + 1
                result_string = result_string + npermanent_string
            count = count + 1
            index = index + 1
    if index == 0:
        print("\nВаша строка состояла только из пробелов")
    return result_string, res_flag


# Тело программы
user_string = input("\nВведите 1 слово >>> ")
changed_word, flag = first_char(user_string)
if flag != 0:
    print("Введенное слово не начинается с буквы или пустое. Слово вернется без изменений")
print("Результат преобразования слова: ", changed_word)
user_string = input("\nВведите несколько слов через пробел >>> ")
changed_word, flag = prepare_list(user_string)
if flag != 0:
    print("Введенная строка содержит слова, которые не начинаются с буквы или пустые. Они вернутся без изменений")
print("Результат преобразования набора слов: ", changed_word)
