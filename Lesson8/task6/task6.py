# This Python file uses the following encoding: utf-8
import Lesson8.task456 as t


def check_float(num):
    try:
        if float(num) != "":
            num = float(num)
        elif float(user_eq) == "":
            num = 0
    except ValueError:
        print(f"\nЗначение {num} невозможно конвертировать в число\nУстановлено значение по-умолчанию: 1")
        num = 1
    return num


def check_bool(value):
    if value.lower() == "true" or value == "1" or value.lower() == "yes":
        return True
    elif value.lower() == "false" or value == "0" or value.lower() == "no":
        return False
    else:
        print("\nВведено значение не из списка, установлено значение по-умолчанию - True")
        return True


user_scan_list = []
user_print_list = []
user_xer_list = []

user_eq = ""

while user_eq.lower() != "stop":
    user_eq = input("\nВведите ID оргтехники, чтобы ввести данные\n1 - Принтер\n2 - Ксерокс\n3 - Сканнер"
                    "\nдля выхода введите stop >>> ")
    if user_eq.lower() == "stop":
        break
    elif user_eq == "1":
        model = input("\nВведите модель Принтера >>> ")
        price = input("Введите цену Принтера >>> ")
        price = check_float(price)
        in_warehouse = input("Находится ли Принтер на складе?\nЕсли да, введите одно из значений: True, Yes, 1"
                             "\nЕсли нет - введите: False, No, 0\n>>> ")
        in_warehouse = check_bool(in_warehouse)
        if in_warehouse:
            division_name = ""
        else:
            division_name = input("Введите название подразделения, где находится Принтер >>> ")
        is_color = input("Доступна ли цветная печать?\nЕсли да, введите одно из значений: True, Yes, 1"
                         "\nЕсли нет - введите: False, No, 0\n>>> ")
        is_color = check_bool(is_color)
        two_sided = input("Доступна ли двусторонняя печать?\nЕсли да, введите одно из значений: True, Yes, 1"
                          "\nЕсли нет - введите: False, No, 0\n>>> ")
        two_sided = check_bool(two_sided)
        user_print = t.Printer(model, price, in_warehouse, division_name, is_color, two_sided)
        user_print_list.append(user_print)
    elif user_eq == "2":
        model = input("\nВведите модель Ксерокса >>> ")
        price = input("Введите цену Ксерокса >>> ")
        price = check_float(price)
        in_warehouse = input("Находится ли Ксерокс на складе?\nЕсли да, введите одно из значений: True, Yes, 1"
                             "\nЕсли нет - введите: False, No, 0\n>>> ")
        in_warehouse = check_bool(in_warehouse)
        if in_warehouse:
            division_name = ""
        else:
            division_name = input("Введите название подразделения, где находится Ксерокс >>> ")
        is_color = input("Доступна ли цветная печать?\nЕсли да, введите одно из значений: True, Yes, 1"
                         "\nЕсли нет - введите: False, No, 0\n>>> ")
        is_color = check_bool(is_color)
        return_to_email = input("Доступна ли отправка на email?\nЕсли да, введите одно из значений: True, Yes, 1"
                                "\nЕсли нет - введите: False, No, 0\n>>> ")
        return_to_email = check_bool(return_to_email)
        user_xer = t.Xerox(model, price, in_warehouse, division_name, is_color, return_to_email)
        user_xer_list.append(user_xer)
    elif user_eq == "3":
        model = input("\nВведите модель Сканнера >>> ")
        price = input("Введите цену Сканнера >>> ")
        price = check_float(price)
        in_warehouse = input("Находится ли Сканнер на складе?\nЕсли да, введите одно из значений: True, Yes, 1"
                             "\nЕсли нет - введите: False, No, 0\n>>> ")
        in_warehouse = check_bool(in_warehouse)
        if in_warehouse:
            division_name = ""
        else:
            division_name = input("Введите название подразделения, где находится Сканнер >>> ")
        two_sided = input("Доступна ли двусторонняя печать?\nЕсли да, введите одно из значений: True, Yes, 1"
                          "\nЕсли нет - введите: False, No, 0\n>>> ")
        two_sided = check_bool(two_sided)
        no_list_protection = input("Есть ли защита от пустого лотка?\nЕсли да, введите одно из значений: True, Yes, 1"
                                   "\nЕсли нет - введите: False, No, 0\n>>> ")
        no_list_protection = check_bool(no_list_protection)
        user_scan = t.Scanner(model, price, in_warehouse, division_name, two_sided, no_list_protection)
        user_scan_list.append(user_scan)
    elif user_eq == "":
        print(f"\nВведенный ID {user_eq} не существует")
    else:
        print(f"\nВведенный ID {user_eq} не существует")

my_Warehouse = t.OfficeEquipmentWarehouse(10, 8, 10)
my_Warehouse.store(user_print_list, user_xer_list, user_scan_list)

print("\nСохраненные данные об оргтехнике: ")
for el in user_print_list:
    el.print_info()

for el in user_xer_list:
    el.print_info()

for el in user_scan_list:
    el.print_info()

print("\nСтатистика по принтерам: ", my_Warehouse.equipment_count(user_print_list))
print("\nСтатистика по ксероксам: ", my_Warehouse.equipment_count(user_xer_list))
print("\nСтатистика по сканнерам: ", my_Warehouse.equipment_count(user_scan_list))
