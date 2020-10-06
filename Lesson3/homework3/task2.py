user_name = input("Введите имя >>> ")
user_surname = input("Введите фамилию >>> ")
user_year = input("Введите год >>> ")
user_city = input("Введите город >>> ")
user_email = input("Введите почту >>> ")
user_phone = input("Введите номер телефона >>> ")


def user_info(name, surname, year, city, email, phone):
    try:
        year = int(year)
        print(
            f"Имя пользователя - {name}, Фамилия - {surname}, Год - {year}, "
            f"Город - {city}, Почта - {email}, Телефон - {phone}")
    except ValueError:
        print(f"Вы ввели некорректное значение для параметра год! Результат по умолчанию - пустое значение")
        print(
            f"Имя пользователя - {name}, Фамилия - {surname}, Год - , "
            f"Город - {city}, Почта - {email}, Телефон - {phone}")


user_info(user_name, user_surname, user_year, user_city, user_email, user_phone)
