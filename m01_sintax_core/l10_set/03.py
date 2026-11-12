def add_element(collection, element):
    if type(collection) is set:
        collection.add(element)
    else:
        print("Ошибка: предоставленная коллекция не является множеством")

my_set = {1, 2, 3}
add_element(my_set, 4)  # Элемент будет добавлен
add_element([1, 2, 3], 4)  # Выведет ошибку