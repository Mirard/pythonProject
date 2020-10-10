# Задача №4 Представлен список чисел. Определить элементы списка,
# не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
import random

num_list = []
result_list = []

num_length = random.randint(0, 20)
index = 0

while index < num_length:
    num_list.append(random.randint(0, 20))
    index = index + 1
for elem in num_list:
    if num_list.count(elem) == 1:
        result_list.append(elem)

print(f"Исходный список: {num_list}\nПолученный список: {result_list}")
