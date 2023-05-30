# [1,2,3,1,3,4,6,5,3] get unique nums from list with basic constructs

nums = [1, 2, 3, 1, 3, 4, 6, 5, 3]
unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)