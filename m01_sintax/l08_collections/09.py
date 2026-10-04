# Использование копии списка

numbers = [1, -1, 2, -2, 3, -3]

# Создаём копию списка для безопасной итерации
for number in numbers.copy():
    if number < 0:
        numbers.remove(number)

print(numbers)