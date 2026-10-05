my_list = [0, 1, 2, 3, 4, 5, 6]

print("# получение подсписка с 3 по 7 элемент")
sub_list = my_list[2:7]
print(sub_list)


print("# получение каждого второго элемента")
step_list = my_list[0:10:2]
print(step_list)


numbers = [432, 45, 32, 6, 43, 7, 5, 34, 7]

print("# до индекса 5 не включительно")
print(numbers[:5])

print("# с индекса 2 включительно и до конца")
print(numbers[2:])

print("# с индекса 2 включительно и до индекса 5 не включительно")
print(numbers[2:5])