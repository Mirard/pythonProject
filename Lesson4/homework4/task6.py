# Задание №6 Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
import random
import itertools


# Часть а
def gen10(n):
    new_list = []
    index = 0
    for el in itertools.count(n):
        if index > 10:
            break
        new_list.append(el)
        index = index + 1
    return new_list


gen_list = gen10(random.randint(0, 1000))
print("Сгенерированный список: ", gen_list)


# Часть б
def regen_list(user_list):
    new_list = []
    index = 0
    for el in itertools.cycle(user_list):
        if index > 30:
            break
        new_list.append(el)
        index = index + 1
    return new_list


re_list = regen_list(gen_list)
print("Список с повторениями: ", re_list)
