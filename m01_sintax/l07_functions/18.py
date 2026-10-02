# Использование **kwargs
#
# **kwargs работает аналогично *args, но для аргументов, заданных по имени, представленных в виде словаря.
# Это позволяет функции принимать любое количество именованных аргументов:

def print_named_items(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_named_items(fruit='apple', number=1)