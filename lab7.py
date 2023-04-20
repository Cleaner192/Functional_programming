# d = {"one": 1, "two": 2, "three": 3, "four": 4}
# geting = d.get("two")
# print(geting)
# print(list(d))
# print(d.values())
# print(d.items())
# del d["two"]
# print(d.items())

#################   1 задание    ################## 
# n = int(input("Введите число элементов в словаре: "))
# dictionary = {}


# for i in range(n):
#     country, river = input().split()
#     dictionary[river] = country


# for river in input().split():
#     if river in dictionary:
#         print("{} - {}".format(river, dictionary[river]))
#     else:
#         print("{} не найдена в словаре".format(river))


# new_country, new_river = input().split()
# dictionary[new_river] = new_country
#################   2 задание    ################## 

# commentators = set()

# while True:
#     line = input().strip()
#     if not line:
#         break

#     name, _ = line.split(':')
#     commentators.add(name.strip())

# print(len(commentators))




#################   3 задание    ################## 
# phone_number = {}
 
# for i in range(int(input())):
#     noomer = input().split()
#     if noomer[1] not in phone_number:
#         phone_number[noomer[1]] = []
#     phone_number[noomer[1]].append(noomer[0])
 
# for i in range(int(input())):
#     name = input()
#     if name in phone_number:
#         print(*phone_number[name])
#     else:
#         print('Нет в телефонной книге')

#################   4 задание    ################## 
n = int(input('Кол-во сотрудников: '))
vacations = {}

for i in range(n):
    name, day, month = input('Введите имя, день и месяц через запятую: ').split()
if month not in vacations:
    vacations[month] = []
vacations[month].append(name)

requested_month = input('Введите месяц для поиска: ')
if requested_month in vacations:
    print(' '.join(vacations[requested_month]))
else:
    print('Нет сотрудников в отпуске в этом месяце')
