# Оператор ^

set1 = {1, 2, 3}
set2 = {3, 4, 5}
s_diff = set1 ^ set2
print(s_diff)  # Вывод: {1, 2, 4, 5}


# Использование функции symmetric_difference ()

set1 = {1, 2, 3}
set2 = {3, 4, 5}
s_diff = set1.symmetric_difference(set2)
print(s_diff)  # Вывод: {1, 2, 4, 5}