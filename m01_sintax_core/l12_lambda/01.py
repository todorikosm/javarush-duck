# Системные функции.

# Напишите программу, которая создает несколько объектов различных типов и
# использует функции id(), hash(), и dir() для выполнения следующих операций:
# Определить и вывести уникальные идентификаторы объектов с помощью id().
# Вывести хеш-значения хешируемых объектов с помощью hash().
# Вывести список атрибутов и методов объекта с помощью dir().

# Напишите тут ваш код

my_list = list(range(10))
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {
    "name": "Sergey",
    "lastname": "Todoriko"
}

print(id(my_list))
print(id(my_tuple))
print(id(my_set))
print(id(my_dict))

print(hash(my_tuple))

print(dir(my_list))
print(dir(my_tuple))
print(dir(my_set))
print(dir(my_dict))