# tom = ("Алекс", 37, "Google", "software developer")
# print(tom[0])       
# print(tom[1])       
# print(tom[-1]) 


# name, age, company, position = ("Алекс", 37, "Google", "software developer")
# print(name)         
# print(age)         
# print(position)    
# print(company)  

# tom = ("Алекс", 22, "Google")
# for item in tom:
#     print(item)

# my_set = set('Hello') 
# print(my_set.pop())
# print(my_set.discard('o'))

#################   1 задание    ##################  
# Заполните один кортеж десятью случайными целыми числами от 0 до 5
# включительно. Также заполните второй кортеж числами от -5 до 0. Для
# заполнения кортежей числами напишите одну функцию. Объедините
# два кортежа с помощью оператора +, создав тем самым третий кортеж.
# С помощью метода кортежа count() определите в нем количество
# нулей. Выведите на экран третий кортеж и количество нулей в нем.

# import random

# def generate_tuple(start, stop, size):
#     return tuple(random.randint(start, stop) for _ in range(size))
# tuple1 = generate_tuple(0, 5, 10)
# tuple2 = generate_tuple(-5, 0, 10)
# tuple3 = tuple1 + tuple2
# num_zeros = tuple3.count(0)
# print("Кортеж 3:", tuple3)
# print("Число нулей в кортеже 3:", num_zeros)


#################   2 задание    ################## 
# nested_tuple = (3.14, ("Hello, world!", (1+2j, ("Nested tuple!", ()))) )
# print(nested_tuple[1][0])

#################   3 задание    ##################  
# # Создаем список категорий расходов
# expense_categories = ["Транспорт", "Обед", "Развлечение", "Покупки", "Прочее"]

# # Создаем список для хранения расходов за каждый день недели
# weekly_expenses = [[] for _ in range(7)]

# # Вводим расходы за каждый день недели
# for day in range(7):
#     print("Впишите затраты для", ["Понидельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"][day])
#     for category in expense_categories:
#         expense = float(input(category + ": $"))
#         weekly_expenses[day].append(expense)

# # Выводим общий объем расходов за неделю
# total_expenses = 0
# for day in range(7):
#     total_expenses += sum(weekly_expenses[day])
# print("Общий объем расходов в неделю: $", total_expenses)


#################   4 задание    ##################
# Вводятся имена студентов в одну строчку через пробел. На их основе
# формируется кортеж. Отобразите на экране все имена из этого кортежа,
# которые содержат фрагмент "ва". Имена выводятся в одну строку через
# пробел
# s = tuple(input( '-> ' ).lower().split())
 
# print( *tuple(i for i in s if 'ва' in i) )



#################   5 задание    ##################
# Напишите программу, которая любой введенный казахский текст из
# кириллицы переводит в латиницу

# print('Введите текст')
# text = str(input())

 
# def transliterate(text):
#     translate =  {"а": "a", "ә": "á", "б": "b", "в": "v", "г": "g",    "ғ": "ǵ", "д": "d", "е": "e", "ё": "io", "ж": "j",    "з": "z", "и": "i", "й": "ı", "к": "k", "қ": "q",    "л": "l", "м": "m", "н": "n", "ң": "ń", "о": "o",    "ө": "ó", "п": "p", "р": "r", "с": "s", "т": "t",    "у": "ý", "ұ": "u", "ү": "ú", "ф": "f", "х": "h",    "һ": "h", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch",    "ъ": "", "ы": "y", "і": "i", "ь": "", "э": "e",    "ю": "iu", "я": "ia"}
    
#     # translate ="a b c d e f g h i j k l m n o p q r s t u v w y z"
    

#     # lower chars
#     dic = { chr(kz):translate for kz, translate in zip( \
#         list(range(1072, 1078)) + [1105] + list(range(1078, 1104)), translate.split()) }
 
#     # upper chars
#     dic.update({ chr(kz):translate for kz, translate in zip( \
#         list(range(1040, 1046)) + [1025] + list(range(1046, 1072)), translate.title().split()) })
 
#     new_text = ''
#     for char in text:
#         if char in dic:
#             new_text += dic[char]
#         else:
#             new_text += char
 
#     return new_text
 
# print(transliterate(text))


text = input("Введите текст: ")
translate = {    "а": "a", "ә": "á", "б": "b", "в": "v", "г": "g",    "ғ": "ǵ", "д": "d", "е": "e", "ё": "io", "ж": "j",    "з": "z", "и": "i", "й": "ı", "к": "k", "қ": "q",    "л": "l", "м": "m", "н": "n", "ң": "ń", "о": "o",    "ө": "ó", "п": "p", "р": "r", "с": "s", "т": "t",    "у": "ý", "ұ": "u", "ү": "ú", "ф": "f", "х": "h",    "һ": "h", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch",    "ъ": "", "ы": "y", "і": "i", "ь": "", "э": "e",    "ю": "iu", "я": "ia"}
translit_text = ""
for char in text:    
    if char.lower() in translate:        
        if char.isupper():           
             translit_text += translate[char.lower()].capitalize()        
        else:            
             translit_text += translate[char]    
    else:        
        translit_text += char
        print("Текст в латинице: ", translit_text)


