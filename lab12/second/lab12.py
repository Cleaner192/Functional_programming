
# Задача 2

# Открываем файл с именами девочек и записываем их в список
with open("Girls.txt", "r") as file1:
    girls = file1.read().splitlines()

# Открываем файл с именами мальчиков и записываем их в список
with open("Boys.txt", "r") as file2:
    boys = file2.read().splitlines()

# Получаем ввод от пользователя
name_input = input("Введите имя мальчика, имя девочки или оба имени через пробел: ")

# Разделяем ввод пользователя на список имен
names = name_input.split()

# Проверяем, являются ли введенные имена популярными именами
for name in names:
    if name in girls:
        print(name, "является популярным именем для девочек")
    elif name in boys:
        print(name, "является популярным именем для мальчиков")
    else:
        print(name, "не является популярным именем")



        

