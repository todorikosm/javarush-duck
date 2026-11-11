# Рассмотрим пример, в котором мы сохраняем индексы и элементы множества в списке для дальнейшей обработки.
my_set = {"apple", "banana", "cherry"}

indexed_elements = [(index, element) for index, element in enumerate(my_set)]
print(indexed_elements)


# Рассмотрим пример, в котором мы выполняем определенную операцию над элементами множества, используя их индексы.
my_set = {1, 2, 3, 4, 5}
squared_elements = {}

for index, element in enumerate(my_set):
    squared_elements[index] = element ** 2

print(squared_elements)


# В принципе при работе с множествами можно использовать и цикл while.
my_set = {"убрать дом", "помыть посуду", "купить хлеба"}
while len(my_set) > 0:
    task = my_set.pop()
    print(task)
