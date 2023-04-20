#################   1 задание    ################## 
# import random

# # Создаем список случайных чисел
# numbers = [random.randint(1, 100) for _ in range(10)]
# print(f"Исходный список: {numbers}")

# # 1. Сортировка списка
# sorted_numbers = sorted(numbers)
# print(f"Сортированный список: {sorted_numbers}")

# # 2. Минимальное и максимальное число
# min_number = min(sorted_numbers)
# max_number = max(sorted_numbers)
# print(f"Минимальное число: {min_number}")
# print(f"Максимальное число: {max_number}")

# # 3. Сумма чисел в списке
# sum_of_numbers = sum(sorted_numbers)
# print(f"Сумма чисел: {sum_of_numbers}")

# # 4. Среднее арифметическое
# average_number = sum_of_numbers / len(sorted_numbers)
# print(f"Среднее арифметическое: {average_number}")

# # 5. Возведение в квадрат
# squared_numbers = list(map(lambda x: x ** 2, sorted_numbers))
# print(f"Квадраты чисел: {squared_numbers}")

# # 6. Отбор четных чисел
# even_numbers = list(filter(lambda x: x % 2 == 0, sorted_numbers))
# print(f"Четные числа: {even_numbers}")

# # 7. Проверка на четность
# all_even = all(map(lambda x: x % 2 == 0, sorted_numbers))
# print(f"Все числа четные: {all_even}")

# # 8. Есть ли в списке числа кратные 3
# has_multiple_of_3 = any(map(lambda x: x % 3 == 0, sorted_numbers))
# print(f"Есть числа, кратные 3: {has_multiple_of_3}")

# # 9.Вывод числе по индексам
# for index, number in enumerate(sorted_numbers):
#     print(f"Число под индексом {index}: {number}")

# # 10. Объединение списков
# letters = ["a", "b", "c", "d", "e"]
# letter_values = [1, 2, 3, 4, 5]
# letter_dict = dict(zip(letters, letter_values))
# print(f"Словарь: {letter_dict}")

#################   2.2    ################## 
# Создаем список чисел
# numbers = [10, 25, 30, 45, 50]

# # Проверяем, есть ли хотя бы одно число, кратное 5
# if any(num % 5 == 0 for num in numbers):
#     print("В списке есть число, кратное 5")
# else:
#     print("В списке нет чисел, кратных 5")

# # Проверяем, являются ли все числа в списке кратными 5
# if all(num % 5 == 0 for num in numbers):
#     print("Все числа в списке кратны 5")
# else:
#     print("Не все числа в списке кратны 5")

#################   2.4    ################## 
def knapsack_dp(weights, values, max_weight):
    n = len(weights)
    dp_table = [[0 for j in range(max_weight + 1)] for i in range(n + 1)]
    
    for i, (weight, value) in enumerate(zip(weights, values), start=1):
        for j in range(1, max_weight + 1):
            if j >= weight:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i-1][j-weight] + value)
            else:
                dp_table[i][j] = dp_table[i-1][j]
    
    return dp_table[n][max_weight]
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
max_weight = 7

max_value = knapsack_dp(weights, values, max_weight)
print("Максимальная стоимость, которую можно унести в рюкзаке:", max_value)

# Здесь мы создаем матрицу размером (n+1) x (capacity+1) и заполняем ее нулями. Затем мы заполняем эту матрицу, используя динамическое программирование, чтобы найти максимальную стоимость, которую можно унести в рюкзаке. Для этого мы используем формулу:

# Если вес i-го предмета меньше или равен j (текущий вес рюкзака), то мы можем взять этот предмет или не взять его. Если мы не берем этот предмет, то максимальная стоимость будет равна стоимости максимальной стоимости, которую можно унести в рюкзаке, не включая i-й предмет. Если мы берем этот предмет, то максимальная стоимость будет равна сумме стоимости i-го предмета и максимальной стоимости, которую можно унести в рюкзаке, не включая i-й предмет и учитывая оставшуюся грузоподъемность.
# Если вес i-го предмета больше, чем j (текущий вес рюкзака), то мы не можем взять этот предмет, и максимальная стоимость будет равна максимальной стоимости, которую можно унести в рюкзаке, не включая i-й предмет.
# Затем мы возвращаем максимальную стоимость, которую можно унести в рюкзаке, находясь в последней ячейке матрицы.
