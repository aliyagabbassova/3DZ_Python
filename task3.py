# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random 
n = int(input("Введите длину списка: ")) 
my_list = [round(random.uniform(0, 100), 3) for i in range(n)] 
print(my_list) 
 
result = [0]*n 
for i in range(len(result)): 
    result[i] = round(my_list[i] % 1, 3) 
# print(result) 
print(f"Разница максимальной и минимальной дробной частью значений равна {round(max(result)-min(result),3)}") 

