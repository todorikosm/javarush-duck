# базовая распаковка
numbers = (1, 2, 3, 4, 5)


def calculate(numbers):
    sum = 0
    min = numbers[0]
    max = numbers[0]

    for i in numbers:
        sum += 1
        if i > max:
            max = i
        if i < min:
            min = i

    avg = round(sum / len(numbers), 2)

    return sum, min, max, avg


sum, min, max, avg = calculate([12, 43, 6, 54, 23, 6, 43])
_, min_res, max_res, _ = calculate([12, 43, 6, 54, 23, 6, 43])
sum_res, *result, avg_res = calculate([12, 43, 6, 54, 23, 6, 43])
sum_res, *_ = calculate([12, 43, 6, 54, 23, 6, 43])

print(min_res, max_res)
print("===========") 
print(sum_res, avg_res)
print("===========")
print(result)
