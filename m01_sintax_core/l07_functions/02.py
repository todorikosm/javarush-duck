def calculate(numbers):
    result = 0
    for number in numbers:
        result += number
    return result
print(calculate([1,2,3,4,5]))


def calculate(numbers):
    result = 0
    for number in numbers:
        result += number
        avg = result / len(numbers)
    return result, avg  # возвращается кортеж
print(calculate([1,2,3,4,5]))
