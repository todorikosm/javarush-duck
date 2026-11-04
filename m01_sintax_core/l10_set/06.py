my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_set = {x for x in my_set if x % 2 == 0}
print(even_set)  # Вывод: {2, 4, 6, 8, 10}

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, "apple", "banana"}
even_set = {x for x in my_set if type(x) == str}
print(even_set)  # Вывод: {"apple", "banana"}