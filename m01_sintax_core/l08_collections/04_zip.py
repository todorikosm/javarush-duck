products = ["велосипеды", "лыжи", "коньки", "скейт", "самокат"]
prices = [120000, 80000, 35000, 12000, 0]
discounts = [0.12, 0.05, 0.1, 0.5, 0.14]

for title, price, discount in zip(products, prices, discounts):
    print(f"{title}: {price} {discount }")