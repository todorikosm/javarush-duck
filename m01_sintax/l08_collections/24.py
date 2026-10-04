# Фильтрация

# Напишите программу, которая создает список из 20 случайных чисел в диапазоне от 1 до 100
# с использованием List Comprehension.
# Затем с использованием List Comprehension создает новый список, содержащий только четные числа
# из исходного списка.
# Программа должна вывести оба списка.

# Напишите тут ваш код

from random import randrange

n = 20

my_list = [randrange(1, 101) for i in range(n)]
print(my_list)

new_list = [x for x in my_list if x % 2 == 0]
print(new_list)