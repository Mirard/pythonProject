viruchka = float(input("Ввведите выручку предприятия в рублях >>> "))
izdergki = float(input("Введите издержки предприятия в рублях >>> "))
sotrudniki = 0
if viruchka > izdergki:
    print("Фирма работает в прибыль")
    rent = (viruchka - izdergki) / viruchka
    print("Рентабельность фирмы: ", rent)
    while sotrudniki <= 0:
        sotrudniki = int(input("Введите численность сотрудников фирмы >>> "))
    pribil_chelovek = (viruchka - izdergki) / sotrudniki
    print("Прибыль фирмы в рассчете на 1 сотрудника: ", pribil_chelovek)
elif viruchka == izdergki:
    print("Фирма работает в 0")
else:
    print("Фирма работает в убыток")
