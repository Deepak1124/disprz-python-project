# Build a counter generator

def counter_generator(list):
  count = 0
  for ele in list:
    count += 1
    yield ele, count

list = [1, 2, 3, 4, 5]

for ele, count in counter_generator(list):
  print(ele, count)