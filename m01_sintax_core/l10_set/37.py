# Метод find(substring):
# Возвращает индекс первого вхождения подстроки в строку или -1, если подстрока не найдена.
text = "hello world"
index = text.find("world")
print(index)  # Вывод: 6


# Метод index(substring):
# Аналогично find, но в случае отсутствия подстроки бросает исключение ValueError.
text = "hello world"
try:
    index = text.index("world")
    print(index)  # Вывод: 6
except ValueError:
    print("Substring not found")


# Метод replace(old, new):
# Заменяет все вхождения подстроки old на подстроку new.
text = "hello world"
replaced_text = text.replace("world", "everyone")
print(replaced_text)  # Вывод: "hello everyone"


# Метод startswith(prefix):
# Проверяет, начинается ли строка с указанного префикса.
text = "hello world"
print(text.startswith("hello"))  # Вывод: True


# Метод endswith(suffix):
# Проверяет, заканчивается ли строка указанным суффиксом.
text = "hello world"
print(text.endswith("world"))  # Вывод: True