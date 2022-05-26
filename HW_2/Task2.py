# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


N = int(input("Ввeдите число: "))
fac = 1
res = []
for i in range(N):
    res.append(fac*(i+1))
    fac = fac*(i+1)
print(res)