my_list = [0, 1, 2, 3, 4, 5, 6]

print("# получение подсписка с 3 по 7 элемент")
sub_list = my_list[2:7]
print(sub_list)


print("# получение каждого второго элемента")
step_list = my_list[0:10:2]
print(step_list)


print("# до 4-го индекса включительно")
numbers = [432, 45, 32, 6, 43, 7, 5, 34, 7]
print(numbers[:5])

print("# с индекса 2 и до конца")
print(numbers[2:])