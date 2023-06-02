# Create function to generate data randomly with python standard library


import random

def generate_random_data(min_value, max_value, size):
    random_numbers = []
    for i in range(size):
        random_numbers.append(random.randint(min_value, max_value))

    return random_numbers


print(generate_random_data(2,35,5))