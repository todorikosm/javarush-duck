my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)  # Вывод: {1, 2, 3, 4, 5}

set1 = {'apple', 'banana'}
set2 = {'banana', 'cherry'}
set3 = {'cherry', 'date'}

combined_set = set1 | set2 | set3
print(combined_set)  # Вывод: {'apple', 'banana', 'cherry', 'date'}