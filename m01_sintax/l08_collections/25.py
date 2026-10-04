# Сортировки

# Напишите программу, которая создает список из 10 случайных чисел в диапазоне от 1 до 100.
# Затем сортирует его по возрастанию и убыванию.
# Программа должна вывести исходный список, отсортированный по возрастанию и по убыванию списки.

# Напишите тут ваш код

from random import randrange

n = 10

my_list = [randrange(1, 101) for i in range(n)]
print(my_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)