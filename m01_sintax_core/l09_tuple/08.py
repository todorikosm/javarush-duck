import random
# Просто и сложно одновременно

# Создай 5 кортежей с разной длинной: 0 элементов, 1 элемент, 5 элементов, 100 элементов, 1000 элементов.
# Выведи их на экран.

# Напишите тут ваш код

tuple1 = ()
tuple2 = (1,)
tuple3 = tuple(random.randint(1, 1000) for _ in range(5))  # 5 случайных чисел
tuple4 = tuple(range(1, 101)) # Способ 2: С помощью `range()` и `tuple()`
tuple5 = tuple(i**2 for i in range(1, 1001)) #С использованием генератора

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)
