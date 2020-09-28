num = -1
num_list = []

while num <= 0:
    num = int(input("Введите целое положительное число >>> "))

while (num // 10) != 0:
    part_num = num % 10
    num_list.append(part_num)
    num = num // 10
# Добавляем первую цифру в список
part_num = num % 10
num_list.append(part_num)

num_list.sort()
num_list.reverse()
print("Наибольшая цифра в числе: ", num_list[0])
