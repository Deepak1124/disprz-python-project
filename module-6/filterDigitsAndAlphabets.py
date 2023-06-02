# [1, “a”, 2, “b”, 3, “c”] filter digits and alphabets separately using inbuilt
# functions like map, filter or reduce

from functools import reduce

data = [1, "a", 2, "b", 3, "c"]

# with filter
digits = list(filter(lambda x: isinstance(x, int), data))
alphabets = list(filter(lambda x: isinstance(x, str), data))

# with reduce
digits = list(reduce(lambda acc, x: acc + [x] if isinstance(x, int) else acc, data, []))
alphabets = list(reduce(lambda acc, x: acc + [x] if isinstance(x, str) else acc, data, []))

print("Digits:", digits)
print("Alphabets:", alphabets)

