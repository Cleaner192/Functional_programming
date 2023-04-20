import os.path
from transliterate import translit, get_available_language_codes

# Получение текущей директории
current_dir = os.path.abspath(os.path.curdir)
print("Текущая директория:", current_dir)

# Соединение двух путей
path1 = "/home/user"
path2 = "Documents"
result_path = os.path.join(path1, path2)
print("Результат объединения путей:", result_path)

# Разделение пути на директорию и имя файла
full_path = "/home/user/Documents/example.txt"
dirname, filename = os.path.split(full_path)
print("Директория:", dirname)
print("Имя файла:", filename)

# Проверка наличия файла
file_path = "/home/user/Documents/example.txt"
if os.path.exists(file_path):
    print("Файл существует")
else:
    print("Файл не найден")

# Получение списка доступных языков для транслитерации
languages = get_available_language_codes()
print("Доступные языки для транслитерации:", languages)

# Транслитерация текста с помощью библиотеки transliterate
text = "Привет, мир!"
translit_text = translit(text, "ru", reversed=True)
print("Транслитерированный текст:", translit_text)

# Использование функции slugify для создания URL-адреса
from transliterate import slugify
url_text = "Тестовый заголовок статьи"
slugified_url = slugify(url_text)
print("URL-адрес:", slugified_url)

# Использование функции detect_language для определения языка текста
from transliterate import detect_language
text = "Hello, world!"
language = detect_language(text)
print("Язык текста:", language)

# Использование функции translit_long для транслитерации текста большой длины
long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
translit_long_text = translit(long_text, "ru", reversed=True, detect_language=True, strict=False)
print("Транслитерированный текст:", translit_long_text)

# Использование функции get_available_language_packs для получения доступных языковых пакетов
from transliterate import get_available_language_packs
language_packs = get_available_language_packs()
print("Доступные языковые пакеты:", language_packs)
