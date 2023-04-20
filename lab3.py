#################   1 задание    ##################  
# print('Ваше первое значение')
# a = int(input()) 
# print('Ваше второе значение')
# b = int(input()) 

# while a<=b:
#     print('Значение:',a)
#     a=a+1


#################   2 задание    ##################  
# print('Ваше первое значение')
# A = int(input())
# print('Ваше второе значение')
# B = int(input() )

# if A<B:                             
#     for i in range(A, B+1):
#         print('Вывод ',i)
# else:                               
#     for i in reversed(range(B, A+1)):
#         print('Вывод ',i)

#################   3 задание    ##################  
# print('Ваше первое значение')
# a = int(input())
# print('Ваше второе значение')
# b = int(input())
# for i in range(a-int((a%2)==0), b-1, -2):
#    print('Вывод ',i)

#################   4 задание    ##################  
import random
print('Введите сколько карт в колоде')
N = int(input())


cntList = list(range(1,N+1))

mylist = list(range(1,N+1))


delNum = random.choice(mylist)
mylist.remove(delNum)


print ( 'Спискок карт без потерянной %s' %(mylist))
print ( 'Потерянная карта %s' % (delNum))

findCard = ((set(cntList)) - (set(mylist)))





# names = ['Bob', 'Alice', 'Guido']
# for index, value in enumerate(names):
#     print(f'{index}: {value}')






# N = int(input('Введите номер: '))
# n_1 = int(input('Выбирайте карту: '))


# for number in range(1, n_1):
#     count = 0
# count += 1
# print(count, end=' ')
# for number in range(n_1 +1, N +1):
#     count1 = n_1
# count1 += 1
# print(count1, end=' ')
# print('Номер потерянной карточки:', n_1)