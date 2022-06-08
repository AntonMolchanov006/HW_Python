# 4. Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) 
# этих двух чисел.

a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
def Nod(a, b):
    while(a%b != 0):
        temp = a%b
        a = b
        b = temp
    return b


NOK = (a*b)/Nod(a, b)
print(NOK)
