# Четкий но случайный

# Напишите программу, которая создает множество из 10 случайных чисел в диапазоне от 1 до 100.
# Программа должна получить подмножество всех четных чисел из этого множества и вывести его.

# Напишите тут ваш код

import random

random_set = set()
while len(random_set) < 10:
    random_set.add(random.randint(1, 100))

even_set = {x for x in random_set if x % 2 == 0}
print(even_set)

