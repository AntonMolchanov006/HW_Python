# 3. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

string_of_numbers = '75 58 84 63 5 54 73 15'
print(string_of_numbers)
string_of_numbers.split( )
ls = string_of_numbers.split(' ')
maxim = int(ls[0])
minim = int(ls[0])
for item in ls:
    if(int(item) > maxim):
        maxim = int(item)
    elif(int(item) < minim):
        minim = int(item)

print(f'максимальное число равно: {maxim}')
print(f'минимальное число равно: {minim}')

