a = 41
c = 11119
m = 11113
seed = 1


def get_next_random():
    global seed
    seed = (a * seed + c) % m
    return seed

for t in range(1000):
    x = get_next_random()
    print(x)