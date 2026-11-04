# Детектив

# Напиши функцию set_detector, которая проходится по списку(кортежу) своих аргументов и определяет
# - есть среди них множество или нет.
# Вызови функцию set_detector с разными вариантами параметров (с множеством и без).

# Напишите тут ваш код

def set_detector(*args):
    for arg in args:
        if type(arg) is set:
            return True
    return False


my_tuple = ("1", 1, {1, 2, 3})
my_tuple2 = ("1", 1)

set_detector("1", 1, {1, 2, 3})
set_detector("1", 1)



# my_tuple = (1, 2, 3, 2, 4, 2, 5)
# search_value = 2
# indices = []
#
# for index, value in enumerate(my_tuple):
#     if value == search_value:
#         indices.append(index)
#
# print(f"Значение {search_value} встречается на индексах: {indices}")