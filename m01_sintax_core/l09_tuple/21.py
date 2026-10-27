# Этот код найдет все индексы, где значение 2 встречается в кортеже:

my_tuple = (1, 2, 3, 2, 4, 2, 5)
search_value = 2
indices = []

for index, value in enumerate(my_tuple):
    if value == search_value:
        indices.append(index)

print(f"Значение {search_value} встречается на индексах: {indices}")
