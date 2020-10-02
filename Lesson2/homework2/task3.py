month_list = (
    'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима')
year = {"зима": (1, 2, 12), "весна": (3, 4, 5), "лето": (6, 7, 8), "осень": (9, 10, 11)}
year_month = year.keys()
user_val = input("Введите порядковый номер месяца >>> ")

# Решение списком
print("\nРешение списком")
try:
    user_num = int(user_val)
    if 0 < user_num < 13:
        print(f"Месяц {user_num} относится к времени года: ", month_list[user_num - 1])
    else:
        print(f"Месяца с порядковым номером {user_num}\nне существует")
except ValueError:
    print(f"Месяца с порядковым номером: {user_val}\nне существует")

# Решение словарем
print("\nРешение словарем")
count = 0
index = 0
try:
    user_num = int(user_val)
    for pairs in year.items():
        for season in pairs:
            for item in season:
                if item == user_num:
                    print(f"Месяц {user_num} относится к времени года: ", pairs[index-1])
                    count = count + 1
                    break
            index = index + 1
        index = 0
    if count == 0:
        print(f"Месяца с порядковым номером: {user_num}\nне существует")
except ValueError:
    print(f"Месяца с порядковым номером: {user_val}\nне существует")
