# Рассмотрим пример, где мы фильтруем данные на основе индексов, оставляя только элементы с чётными индексами.

my_tuple = ('a', 'b', 'c', 'd', 'e', 'f')

filtered_tuple = tuple(value for index, value in enumerate(my_tuple) if index % 2 == 0)
print(f"Кортеж с элементами на чётных индексах: {filtered_tuple}")