
# [“name512”, “same1example”, “joy18full”] replace the digits from string inside list

str_list = ["name512", "same1example", "joy18full"]

updated_str_list = []

for str in str_list:
    updated_str = ""
    for char in str:
        if not char.isdigit():
            updated_str += char
    updated_str_list.append(updated_str)

print(updated_str_list)
