words = ["велосипеды", "лыжи", "коньки", "скейт"]

for index, value in enumerate(words):
    print(index, value)

print("=================")

for value in enumerate(words, 1):
    print(value)