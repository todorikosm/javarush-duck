# Вот более практический пример использования nonlocal для создания счётчика:

def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = create_counter()
print(counter())  # Выведет 1
print(counter())  # Выведет 2
print(counter())  # Выведет 3