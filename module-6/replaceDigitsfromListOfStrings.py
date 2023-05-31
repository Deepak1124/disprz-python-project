
# [“name512”, “same1example”, “joy18full”] replace the digits from string inside list


import re
str_list = ["name512", "same1example", "joy18full"]
new_str_list = [re.sub('\d+', '', str) for str in str_list]

print(new_str_list)
