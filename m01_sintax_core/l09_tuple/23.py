# Сумма кортежей

# Напишите программу, которая создает кортеж, содержащий несколько вложенных кортежей из целых чисел.
# Программа должна использовать цикл for для вычисления суммы всех элементов во вложенных кортежах и вывести результат.

# Напишите тут ваш код

my_tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_tuple2 = (6, 7, 8, 9, 10)
my_tuple3 = (1, 2, 3, 4, 5)
nested_tuple = (my_tuple1, my_tuple2, my_tuple3)


sum = 0
for inner_tuple in nested_tuple:
    for number in inner_tuple:
        sum = sum + number
print(sum)


# JavaRush

# nested_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
#
# total_sum = 0
# for inner_tuple in nested_tuples:
#     for num in inner_tuple:
#         total_sum += num
#
# print(total_sum)