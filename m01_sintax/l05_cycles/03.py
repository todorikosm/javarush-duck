# Нечетный
from itertools import count

# Напишите программу, которая выводит числа от 1 до 100, пропуская четные числа.
# Используйте цикл while и оператор continue для пропуска четных чисел.

# Напишите тут ваш код

count = 1

while count <= 100:
    if count % 2 == 0:
        count = count + 1
        continue
    else:
        print(count)
        count = count + 1