# Вывод по значению в return

products = ["Велосипеды", "лыжи", "", "Коньки", "лыжи", "", "скейТ", "самокат"]

def handler(word):
    if word == "Велосипеды":
        return 8
    elif word == "лыжи":
        return 6
    elif word == "":
        return 3
    elif word == "Коньки":
        return 2
    elif word == "скейТ":
        return 5
    elif word == "самокат":
        return 9
    else:
        return 0

products.sort(key=handler)
print(products)