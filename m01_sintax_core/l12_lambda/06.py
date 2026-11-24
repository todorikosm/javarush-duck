def make_counter(start = 0):
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

counter = make_counter(10)
print(counter())  # Вывод: 11
print(counter())  # Вывод: 12
print(counter())  # Вывод: 13