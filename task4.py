# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
N = int(input('Введите положительное число: '))
result = []
my_list = list(str(N))[::-1]
    
while True:
    if N != 0:
        if N % 2 == 0:
            result.append(0)
            N = N // 2
        elif N % 2 == 1:
             result.append(1)
             N = N // 2
    else:
        result.reverse()
        print(result)
        break