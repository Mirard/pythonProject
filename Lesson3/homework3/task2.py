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


user_info(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email, phone=user_phone)
