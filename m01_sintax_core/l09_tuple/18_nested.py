# В этом примере nested_tuple содержит кортежи. Мы используем вложенные циклы for для итерации по каждому
# элементу вложенных кортежей. Результат выполнения:

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

for inner_tuple in nested_tuple:
    for number in inner_tuple:
        print(number, end=' ')
    print()