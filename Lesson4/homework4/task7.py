# Задание №7 Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
import random
import math


def fact_calc(fact):
    print("Ваше число: ", fact)
    result = 1
    index = 1
    while index <= fact:
        result = result * index
        index = index + 1
    yield result


rand_num = random.randint(1, 100)
for num in fact_calc(rand_num):
    print(f"Факториал {rand_num}: ", num)
print("Проверка факториала с помощью math.factorial: ", math.factorial(rand_num))
