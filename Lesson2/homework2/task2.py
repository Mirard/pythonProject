user_string = input("Введите строку >>> ")

user_list = list(user_string)
list_len = len(user_list)
index = 0

if list_len == 0:
    print("Вы не ввели значение, перестановка элементов невозможна")
elif list_len == 1:
    print("Вы ввели строку с 1 значением, переставлять нечего, список остается неизменным: ", user_list)
else:
    while index < (list_len // 2) * 2:
        user_list[index], user_list[index + 1] = user_list[index + 1], user_list[index]
        index = index + 2
    print(user_list)
