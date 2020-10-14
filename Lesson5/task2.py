file = open("task2.txt", 'r')
str_count = 0
words_count = []
for string in file.readlines():
    str_count = str_count + 1
    words_count.append(string.count(' ') + 1)
file.close()
print(f"В файле task2.txt {str_count} строк")
ind = 0
while ind < len(words_count):
    print(f"В строке №{ind+1} кол-во слов: {words_count[ind]}")
    ind = ind+1

