def power(exponent):
    def inner(base):
        return base ** exponent
    return inner

square = power(2) # степень
print(square(3))  # Выводит 9

cube = power(3) # степень
print(cube(3)) # Выводит 27