# Задача 3 Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
print("Числа в пределе 20-240, кратные 20 или 21: ", [num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0])
