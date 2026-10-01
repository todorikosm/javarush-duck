words = ["велосипед", "банан", "лыжи", "коньки"]

def sort_by_length(word):
    return len(word)

words.sort(key=sort_by_length)   # передаём функцию, но не вызываем её -- это callback функция 
print(words)