# НДС

# Напишите функцию calculate_total_cost(price, tax=0.2), которая принимает цену товара и необязательный параметр
# налог (по умолчанию 20%).
# Функция должна вычислять и выводить общую стоимость товара с учетом налога.
# Затем напишите программу, которая вызывает эту функцию с различными параметрами.

# Напишите тут ваш код


def calculate_total_cost(price, tax=0.2):
    total = price + (price * tax)
    print(total)
    return total


calculate_total_cost(2000)
calculate_total_cost(3000, 0.3)