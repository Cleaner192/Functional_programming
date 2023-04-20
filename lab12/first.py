
# Задача 1
import os


with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')

# Чтение из файла
with open('example.txt', 'r') as file:
    contents = file.read()
    print('Содержимое файла:', contents)

# Переименование файла
os.rename('example.txt', 'newfile.txt')

# Копирование файла
os.system('cp newfile.txt newfile_copy.txt')

# Удаление файлов
os.remove('newfile.txt')
os.remove('newfile_copy.txt')