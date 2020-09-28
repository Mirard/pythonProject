num = -1
while int(num) < 0:
    num = input("Введите число больше 0 >>> ")
if int(num) == 0:
    print("Сумма 0 + 00 + 000 = 0")
else:
    n = int(num)
    nn = int(num + num)
    nnn = int(num + num + num)
    print(f"Сумма {n} + {nn} + {nnn} = ", n + nn + nnn)
