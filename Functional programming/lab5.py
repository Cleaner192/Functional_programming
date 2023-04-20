

#################################### 1 задача ############################################
# Напишите	программу,	в	которой	предлагается вводить	учащихся	
# различных	групп,	посещающих	секции	по	разным	предметам.	Требуется	
# упорядочить	 список	 по	 различным	 категориям.	 Вывести	 результат	 на	
# экран

# students = {}

# while True:
#     print("Для окончания напишите exit")
#     subject = input("Имя студента: ")
#     if subject == 'exit':
#         break
    
#     group = input("Название предмета: ")
#     if group in students:
#         students[group].append(subject)
#     else:
#         students[group] = [subject]

# for group, subjects in students.items():
#     print("К предмету: ", group)
#     print("Студенты: ", subjects)

# Программа предлагает вводить предметы и группы учеников. Когда вы вводите предмет, программа запрашивает группу, которая его изучает. Если группа уже есть в словаре students, добавляется новый предмет. Если группы еще нет, создается новая запись с этой группой и предметом. Когда вы введете 'q', цикл завершится. В конце программа выведет на экран все группы и предметы, которые они изучают.

#################################### 2 задача ############################################

# grades = {
#     'Azamat': ["Math: 87","Algoritms: 96" ,"English: 70"],
#     'Mary Jane': ["Geometry: 76","1C programming: 50" ,"Mobile programming: 98"],
#     'Arthur Morgan': ["Operating systems: 98","Algoritms: 100" ,"Japan language: 76"]
# }

# def get_grades(name):
#     if name in grades:
#         return grades[name]
#     else:
#         return "Student not found"

# student_name = input("Ваше имя: ")
# print(get_grades(student_name))


# Программа содержит словарь grades, который хранит оценки учеников. Функция get_grades принимает имя ученика и возвращает его оценки, если ученик найден, или сообщение "Student not found", если ученик не найден. Пользователь вводит имя ученика, и результат вызова функции get_grades выводится на экран.

#################################### 3 задача ############################################
# Напишите	программу,	которая	будет	запрашивать	у пользователя	
# целочисленные	 значения	 и сохранять	 их	 в виде	 списка.	 Индикатором
# окончания	 ввода	 значений	 должен	 служить	 ноль.	 Затем	 программа	
# должна	 вывести	 на	 экран	 все	 введенные	 пользователем	 числа	 (кроме	
# нуля)	 в порядке	 возрастания – по	 одному	 значению	 в строке.	
# Используйте	для	сортировки	либо	метод	sort,	либо	функцию	sorted
# data = []
# num = int(input("Введите целое число (0 для окончания ввода): "))
# while num != 0:
#     data.append(num)
#     num = int(input("Введите целое число (0 для окончания ввода): "))
# print(*sorted(data), sep='\r\n', )



#################################### 4 задача ############################################
# Напишите	 программу,	 которая,	 как	 и в предыдущем	 случае,	
# будет	запрашивать	у пользователя	целые	числа	и сохранять	их	в виде	
# списка.	Индикатором	окончания	ввода	значений	также	должен	служить	
# ноль.	На	 этот	раз	необходимо	 вывести	на	 экран	 введенные	значения	 в
# порядке	убывания
# l = []
# while True:
#     n = (int(input('n')))
#     l += [n]
#     if n == 0: break
#     print(sorted(l,reverse=True))


#################################### 5 задача ver 1 ############################################
# from random import shuffle
 
# arr = [*range(1, 50)]
# shuffle(arr)
# print("Номера вашего билета: ", arr[:6])


#################################### 5 задача  ver 2 ############################################
# from random import randrange
# MIN_NUM = 1
# MAX_NUM = 49
# NUM_NUMS = 6
# ticket_nums = []
# for i in range(NUM_NUMS):
#     rand = randrange(MIN_NUM, MAX_NUM + 1)
#     while rand in ticket_nums:
#         rand = randrange(MIN_NUM, MAX_NUM + 1)
#     ticket_nums.append(rand)
# ticket_nums.sort()
# print("Номера вашего билета: ", end = "")
# for n in ticket_nums:
#     print(n, end = " ")
# print()

#################################### 6 задача ############################################
# def is_list_sorted(checked_list):
#     if len(checked_list) == 1:
#         flag = 1
#     for i in range(1, len(checked_list)):
#         if checked_list[i - 1] > checked_list[i]:
#             flag = 1
#         else:
#             flag = 0
#             break
#     if flag == 1:
#         return True
#     for i in range(1, len(checked_list)): 
#         if checked_list[i - 1] < checked_list[i]:
#             flag = 1
#         else:
#             return False
#     if flag == 1:
#         return True
# def main():
#     is_list = input('Введите список для проверки: ').split()
#     if len(is_list) == 0:
#         print('Список пуст')
#         return()
#     if is_list_sorted(is_list):
#         print('Список изначально отсортирован')
#     else:
#         print('Список изначально неотсортирован')
 
# main()