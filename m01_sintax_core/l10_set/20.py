# Индексация

# Напишите программу, которая создает множество из случайных чисел в диапазоне от 1 до 50.
# Затем программа должна вывести все элементы множества вместе с их "индексами", используя функцию enumerate().

# Напишите тут ваш код
import random

count = 50

my_set = {random.randint(1, 50) for _ in range(count)}
print("Множество случайных чисел:", my_set)
print("Размер множества:", len(my_set))

for index, el in enumerate(my_set):
    print(f"Element: {el}, Index: {index}")