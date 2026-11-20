# Обход словаря.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Перебрать все элементы словаря, включая вложенные словари, с использованием циклов.
# Реализовать функцию для обхода всех уровней вложенности и вывода ключей и значений.

# Напишите тут ваш код

contact = {
    "tel": "+79258582575",
    "email": "s.todoriko@yandex.ru",
}

employee_info = {
    "name": "Sergey",
    "lastname": "Todoriko",
    "age": 38,
    "addres": "Moscow",
    "contact": contact
}


def for_dict(dict, indent=0):
    for key, value in dict.items():
        print("  " * indent + str(key) + ": ", end="")
        if isinstance(value, dict):
            for key2, value2 in value.items():
                print(f"{key} --> {key2}: {value2}")

for_dict(employee_info)
