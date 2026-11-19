# # Создание пустого словаря
# empty_dict = {}
#
# # Создание множества с элементами
# unique_items = {
#     "name",
#     "age",
#     "city"
# }
# print(type(unique_items))
# print(unique_items)
#
#
# # Создание словаря из списка кортежей
# person = dict([("name", "John"), ("age", 30), ("city", "New York")])
# print(person)
#
# # Создание словаря с именованными аргументами
# person = dict(name="John", age=30, city="New York")
# print(person)
#
# # Создание словаря с ключами и значением по умолчанию
# keys = ["name", "age", "city"]
# default_value = None
# person = dict.fromkeys(keys, default_value)
# print(person)
#
#
# name = "John"
# age = 30
# city = "New York"
#
# person = {"name": name, "age": age, "city": city}
# print(person)
#
#
# # Создание словаря с помощью генератора словаря
# squares = {x: x**2 for x in range(1, 6)}
# print(squares)
#
#
# # Обращение к значениям в словаре
# person = {"name": "John", "age": 30, "city": "New York"}
# print(person["name"])  # Выведет: John
#
#
# # Использование метода get() для обращения к значениям в словаре
# person = {"name": "John", "age": 30, "city": "New York"}
# print(person.get("name"))  # Выведет: John
# print(person.get("address", "Адрес не найден"))  # Выведет: Адрес не найден
#
#
# # Изменение значений в словаре
# person = {"name": "John", "age": 30, "city": "New York"}
# person["age"] = 31
# print(person)  # Выведет: {'name': 'John', 'age': 31, 'city': 'New York'}
#
#
# # Удаление элемента с помощью del
# person = {"name": "John", "age": 30, "city": "New York"}
# del person["age"]
# print(person)  # Выведет: {'name': 'John', 'city': 'New York'}
#
# # Удаление элемента с помощью pop()
# person = {"name": "John", "age": 30, "city": "New York"}
# age = person.pop("age")
# print(person)  # Выведет: {'name': 'John', 'city': 'New York'}
# print(age)     # Выведет: 30
#
#
# # Проверка наличия ключа в словаре
# person = {"name": "John", "age": 30, "city": "New York"}
# print("name" in person)  # Выведет: True
# print("address" in person)  # Выведет: False
#
#
# # Перебор ключей словаря
# person = {"name": "John", "age": 30, "city": "New York"}
# for key in person:
#     print(key)
#
# # Перебор значений словаря
# for value in person.values():
#     print(value)
#
# # Перебор пар ключ-значение словаря
# for key, value in person.items():
#     print(f"{key}: {value}")
#
#

text = "hello world hello"
word_count = {}
for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)  # Выведет: {'hello': 2, 'world': 1}



students = {
    "123": {"name": "John", "age": 20, "major": "Computer Science"},
    "124": {"name": "Alice", "age": 22, "major": "Mathematics"}
}
print(students["123"]["name"])  # Выведет: John




phone_book = {
    "John": "123-456-7890",
    "Alice": "987-654-3210"
}
print(phone_book["Alice"])  # Выведет: 987-654-3210