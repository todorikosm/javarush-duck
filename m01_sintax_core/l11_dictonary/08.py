# Три проверки.

# Напишите программу, которая создает словарь с информацией о книге (title, author, year).
# Программа должна:
# Проверить наличие ключа "author" с использованием оператора in.
# Проверить наличие ключа "publisher" с использованием метода get().
# Проверить наличие ключа "title" с использованием метода keys().

# Напишите тут ваш код

book_info = {
    "title": "Таинственный остров",
    "author": "Жюль Верн",
    "year": 1817
}

if "author" in book_info.keys():
    print(f"Ключ 'author' присутствует в словаре.")
else:
    print(f"Ключ 'author' НЕ присутствует в словаре.")


value = book_info.get("publisher")
if value is not None:
    print("Ключ 'name' присутствует в словаре.")
else:
    print("Ключ 'name' отсутствует в словаре.")


if "title" in book_info.keys():
    print("Ключ 'name' присутствует в словаре.")
else:
    print("Ключ 'name' отсутствует в словаре.")