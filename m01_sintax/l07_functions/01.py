def power(number, p=2):
    result = number ** p
    return result

side_1 = 4
side_2 = 3

print(power(power(side_1) + power(side_2), 0.5))