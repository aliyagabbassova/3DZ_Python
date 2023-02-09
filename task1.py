# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на 
# нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_1 = [1,2,3,4,5,6,7,8,9,10]
summa = 0
for i in range(1,10): 
    if i % 2 == 1:
        summa+=i
print(summa)


# import random
# summa = 0
# list = [random.randint(1,10) 
# for i in range(10)] 
# i = 0
# if list[i] % 2 == 1:
#     summa += i
# print(list)
# print(summa)