# 2. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

N = int(input("Введите целое число: "))
def Negafibonacci(n: int) -> list:

    Nega_list = []
    Posi_list = [0, 1]
    for i in range(2, n+1):
        Posi_list.append(Posi_list[i-2] + Posi_list[i-1])

    for i in range(n, 0, -1):
        if(i%2 == 0):
            Nega_list.append(Posi_list[i]*(-1))
        else:
            Nega_list.append(Posi_list[i])
    
    
    return Nega_list + Posi_list

print(Negafibonacci(N))
