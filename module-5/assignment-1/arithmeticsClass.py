# Create arithmetics class to calculate avg, mean, mode and standard deviation


import statistics

class Arithmetic:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)

    def calculate_mean(self):
        return statistics.mean(self.numbers)

    def calculate_mode(self):
        return statistics.mode(self.numbers)

    def calculate_standard_deviation(self):
        return statistics.stdev(self.numbers)


numbers = [2, 4, 4, 4, 5, 5, 7, 9]

arithmetics = Arithmetic(numbers)

average = arithmetics.calculate_average()
print("Average:", average)

mean = arithmetics.calculate_mean()
print("Mean:", mean)

mode = arithmetics.calculate_mode()
print("Mode:", mode)

std_deviation = arithmetics.calculate_standard_deviation()
print("Standard Deviation:", std_deviation)
