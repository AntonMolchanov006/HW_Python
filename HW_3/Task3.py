# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19



from os import remove


start_list = [1.1, 1.2, 3.1, 5, 10.01]
def Fraction_difference(lst: list) -> float:
    minimum = 1
    maximum = 0
    for i in range(len(lst)):
        fraction = round((lst[i] - lst[i]//1), 2)
        if fraction == 0:
            continue
        if fraction > maximum:
            maximum = fraction
        if fraction < minimum:
            minimum = fraction
    return(maximum - minimum)

print(Fraction_difference(start_list))