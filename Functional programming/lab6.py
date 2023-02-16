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
nested_tuple = (3.14, ("Hello, world!", (1+2j, ("Nested tuple!", ()))) )
print(nested_tuple[1][1][1][0])

#################   3 задание    ##################  
# # Создаем список категорий расходов
# expense_categories = ["Транспорт", "Обед", "Развлечение", "Покупки", "Прочее"]

# # Создаем список для хранения расходов за каждый день недели
# weekly_expenses = [[] for _ in range(7)]

# # Вводим расходы за каждый день недели
# for day in range(7):
#     print("Enter expenses for", ["Понидельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"][day])
#     for category in expense_categories:
#         expense = float(input(category + ": $"))
#         weekly_expenses[day].append(expense)

# # Выводим общий объем расходов за неделю
# total_expenses = 0
# for day in range(7):
#     total_expenses += sum(weekly_expenses[day])
# print("Общий объем расходов в неделю: $", total_expenses)