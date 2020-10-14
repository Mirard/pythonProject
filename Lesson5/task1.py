f_1 = open("my_file.txt", 'w')
user_words = input("Введите текст, который хотите добавить в файл,\nдля окончания ввода просто нажмите Enter >>> ")
while user_words != '':
    f_1.write(user_words+'\n')
    user_words = input("Введите текст, который хотите добавить в файл,\nдля окончания ввода просто нажмите Enter >>> ")
f_1.close()