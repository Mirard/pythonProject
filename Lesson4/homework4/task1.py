# Запустите main с предустановленными параметрами, чтобы проверить 1е задание
def calculate(user_hours, user_salary, user_bonus):
    try:
        return (user_hours * user_salary) + user_bonus
    except TypeError:
        return
