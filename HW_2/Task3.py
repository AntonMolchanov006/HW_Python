#  Реализуйте случайное перемешивания списка.

# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True ']
# Результат -> [250, 3.14, 'True ', 'Веселый пианист']
import random

Li = ['Веселый пианист', 250, 3.14, 'True ']
random.shuffle(Li)
print(Li)
