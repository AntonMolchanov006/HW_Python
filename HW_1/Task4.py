# 4. Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from math import sqrt


X1 = int(input('Введите координату х для первой точки: '))
Y1 = int(input('Введите координату y для первой точки: '))

X2 = int(input('Введите координату х для второй точки: '))
Y2 = int(input('Введите координату y для второй точки: '))

disX = X1-X2
disY = Y1-Y2
dist = sqrt(disX**2 + disY**2)
print(dist)
