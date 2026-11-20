# Лига Плюща

# Напишите программу, которая создает словарь с информацией о студенте (имя, возраст, университет).
# Программа должна:
# Проверить наличие значения "MIT" с использованием метода values().
# Проверить наличие значения "Harvard" с использованием функции set().
# Проверить наличие значения 22 с использованием генератора.

# Напишите тут ваш код

university_info = {
    "name": "Sergey Todoriko",
    "age": 38,
    "university": "MAMI"
}

if "MIT" in university_info.values():
    print("Значение 'MIT' присутствует в словаре.")
else:
    print("Значение 'MIT' отсутствует в словаре.")


value_set = set(university_info.values())
if "Harvard" in value_set:
    print("Значение 'Harvard' присутствует в словаре.")
else:
    print("Значение 'Harvard' отсутствует в словаре.")


value_to_find = 22
if any(value == value_to_find for value in university_info.values()):
    print(f"Значение {value_to_find} присутствует в словаре.")
else:
    print(f"Значение {value_to_find} отсутствует в словаре.")