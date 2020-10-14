import codecs

# Первая часть
file = codecs.open("task31.txt", "r", "utf-8")
salary_list = []
salary_sum = 0
for string in file.readlines():
    surname = string[0:(string.index(" "))]
    salary = float(string[(string.index(" ") + 1):])
    salary_list.append(salary)
    salary_sum = salary_sum + salary
    if salary < 20000:
        print(f"Оклад сотрудника {surname} менее 20000: ", salary)
print("Средняя зп сотрудников: ", salary_sum/len(salary_list))
file.close()

# Вторая часть
file = codecs.open("task32.txt", "r", "utf-8")
strings_list = []
replace_list = ["Один", "Два", "Три", "Четыре"]
for str1 in file.readlines():
    strings_list.append(str1)

file.close()
file = open("task32result.txt", 'w')
ind = 0
while ind < len(strings_list):
    string_list = strings_list[ind]
    tail_part = string_list[(string_list.index(" ") + 1):]
    file.write(replace_list[ind] + " " + tail_part)
    ind = ind + 1
