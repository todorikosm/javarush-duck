# А теперь давайте найдем максимальный элемент в множестве.

my_set = {1, 2, 3, 4, 5}
max_element = None

for element in my_set:
    if max_element is None or element > max_element:
        max_element = element

print("Максимальный элемент множества:", max_element)



# Давайте создадим новое множество, содержащее только четные числа из исходного множества.
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_set = set()

for element in my_set:
    if element % 2 == 0:
        even_set.add(element)

print("Множество четных чисел:", even_set)