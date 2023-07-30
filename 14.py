# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
n = int(input("Введите число N: "))
result = []
for i in range(1,n):
    result.append(2**i)

print(result)