# Задание №2 Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
import random

num_list = []
result_list = []

num_length = random.randint(0, 20)
index = 0

while index < num_length:
    num_list.append(random.randint(0, 1000))
    if index != 0 and num_list[index] > num_list[index - 1]:
        result_list.append(num_list[index])
    index = index + 1

print(f"Исходный список: {num_list}\nПолученный список: {result_list}")
