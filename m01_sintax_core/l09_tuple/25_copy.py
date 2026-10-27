# Иногда может потребоваться создать изменяемую копию кортежа в виде списка, чтобы внести изменения,
# а затем снова преобразовать его в кортеж.

original_tuple = (1, 2, 3, 4, 5)

temp_list = list(original_tuple)
temp_list.append(6)
copied_tuple = tuple(temp_list)

print(copied_tuple)