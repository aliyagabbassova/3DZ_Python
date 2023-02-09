# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random
list = [random.randint(1,10) 
for i in range(10)] 
for i in range(10):
    multiply = [list[0] * list[9], list[1] * list[8], list[2] * list[7], list[3] * list[6], list[4] * list[5]]
print(list)
print(multiply)
