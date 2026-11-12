# Метод strip():
# Удаляет пробелы в начале и конце строки.
text = "  hello world!  "
cleaned_text = text.strip()
print(cleaned_text)  # Вывод: "hello world!"


# Метод lower():
# Преобразует все символы строки в нижний регистр.
text = "Hello World!"
lower_text = text.lower()
print(lower_text)  # Вывод: "hello world!"


# Метод upper():
# Преобразует все символы строки в верхний регистр.
text = "Hello World!"
upper_text = text.upper()
print(upper_text)  # Вывод: "HELLO WORLD!"


# Метод split(separator):
# Разделяет строку на список подстрок по заданному разделителю.
text = "one,two,three"
parts = text.split(',')
print(parts)  # Вывод: ['one', 'two', 'three']


# Метод join(iterable):
# Объединяет коллекцию строк в одну строку, используя строку-разделитель.
parts = ['one', 'two', 'three']
joined_text = ','.join(parts)
print(joined_text)  # Вывод: "one,two,three"