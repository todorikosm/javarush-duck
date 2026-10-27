numbers = (1, 2, 3, 4, 5)

numbers_list = list(numbers)
numbers_list.append(12)
result = tuple(numbers_list)
print(result)

# numbers как был неизменённым, так и остался.


# или вот так
result2 = numbers + (77,)
print(result2)
