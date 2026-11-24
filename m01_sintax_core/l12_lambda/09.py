# Замыкание.

# Напишите программу, которая создает функцию фильтра с использованием замыканий.
# Программа должна:
# Определить внешнюю функцию make_filter(threshold), которая создает и возвращает внутреннюю функцию filter_func(value).
# Внутренняя функция filter_func(value) должна возвращать True, если value больше threshold.
# Создать несколько функций фильтров с различными пороговыми значениями и
# использовать их для фильтрации списка данных, выводя результат на экран.

# Напишите тут ваш код

def make_filter(threshold):
    def filter_func(value):
        return value > threshold

    return filter_func


filter1 = make_filter(10)
filter2 = make_filter(30)
data = [5, 10, 15, 20, 30, 40]
filtred_data1 = list(filter(filter1, data))
filtred_data2 = list(filter(filter2, data))
print(filtred_data1)
print(filtred_data2)
