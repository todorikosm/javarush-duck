# Случайная функция

# Напишите функцию generate_random_number(), которая выводит на экран случайное число от -200 до 0.

# Напишите тут ваш код

import random

def generate_random_number(a, b):
    value = random.randint(a, b)
    print(value)

generate_random_number(-200, 0)