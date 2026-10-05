from operator import index

products = ["велосипеды", "лыжи", "коньки", "скейт", "самокат", "лыжи"]

# сформировать список, который не содержит лыжи

print([word for word in products if word != "лыжи"]) # отбрасываем обе лыжи


# находит индексы лыж в списке
print([index for index, word in enumerate(products) if word == "лыжи"]) 