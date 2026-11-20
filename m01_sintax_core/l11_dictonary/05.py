# Три способа порыться в словаре.
from operator import truediv

# Напишите программу, которая создает словарь person_dict с информацией о человеке.
# Программа должна:
# Получить значение по ключу с использованием квадратных скобок.
# Безопасно получить значение по ключу с использованием метода get().
# Использовать метод setdefault() для получения значения по ключу и добавления ключа, если он отсутствует.

# Напишите тут ваш код

person_dict = {
    "name": "Sergey",
    "lastname": "Todoriko",
    "age": 38,
    "rainking": 3.8,
    "children": True
}

info1 = person_dict["name"]
print(info1)

info2 = person_dict.get("children")
print(info2)

info3 = person_dict.setdefault("married", True)
print(info3)

print(person_dict)