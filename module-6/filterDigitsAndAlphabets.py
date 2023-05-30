# [1, “a”, 2, “b”, 3, “c”] filter digits and alphabets separately using inbuilt
# functions like map, filter or reduce


data = [1, "a", 2, "b", 3, "c"]

digits = []
alphabets = []

for ele in data:
    if isinstance(ele, int):
        digits.append(ele)
    elif ele.isalpha():
        alphabets.append(ele)

print("Digits:", digits)
print("Alphabets:", alphabets)