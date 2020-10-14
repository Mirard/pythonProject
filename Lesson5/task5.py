import codecs

file = codecs.open("task5.txt", "r", "utf-8")
name = []
lecture = []
practice = []
labs = []
for string in file.readlines():
    name.append(string[0:(string.index(":"))])
    string_tail = string[(string.index(":") + 1):]
    while string_tail[0] == " ":
        string_tail = string_tail[1:]
    count = 0
    main_count = string_tail.count(" ")
    while count <= main_count and len(string_tail) != 0:
        bracket_count = string_tail.count("(")
        tire_count = string_tail.count("-")
        if bracket_count != 0 and tire_count != 0:
            tire_ind = string_tail.index("-")
            bracket_ind = string_tail.index("(")
            if tire_ind > bracket_ind:
                value = string_tail[0:bracket_ind]
            else:
                value = string_tail[0:(tire_ind + 1)]
        elif bracket_count != 0 and tire_count == 0:
            bracket_ind = string_tail.index("(")
            value = string_tail[0:bracket_ind]
        elif bracket_count == 0 and tire_count != 0:
            tire_ind = string_tail.index("-")
            value = string_tail[0:(tire_ind + 1)]
        try:
            space_ind = string_tail.index(" ")
            if count == 0 and value != "-":
                lecture.append(float(value))
            elif count == 0 and value == "-":
                lecture.append(0)
            elif count == 1 and value != "-":
                practice.append(float(value))
            elif count == 1 and value == "-":
                practice.append(0)
            string_tail = string_tail[(space_ind + 1):]
        except ValueError:
            value = string_tail[0:]
            if value == "-":
                labs.append(0)
            else:
                labs.append(float(value[0:(value.index("("))]))
        count = count + 1
file.close()
ind = 0
el_sum = []
my_list = []
while ind < len(name):
    el_sum.append(lecture[ind] + practice[ind] + labs[ind])
    my_list.append((name[ind], el_sum[ind]))
    ind = ind + 1
my_dict = dict(my_list)
print(my_dict)
