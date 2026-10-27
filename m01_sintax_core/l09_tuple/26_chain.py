from itertools import chain

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)

combined_tuple = tuple(chain(tuple1, tuple2, tuple3))
print(combined_tuple)