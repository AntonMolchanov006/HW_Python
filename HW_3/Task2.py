# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. Если остается 1 элемент без пары - умножаем его самого на себя.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

start_list = [2, 3, 4, 5, 6]


def Multiplication(lst: list) -> list:
    new_list = []
    i = 0
    j = len(lst)-1
    if len(lst) % 2 == 0:
        for i in range(len(lst)//2):
            new_list.append(lst[i]*lst[j])
            j = j - 1
            i = i + 1
    else:
        for i in range(len(lst)//2+1):
            new_list.append(lst[i]*lst[j])
            j = j - 1
            i = i + 1
    return new_list


print(Multiplication(start_list))
