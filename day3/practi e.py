from functools import reduce

# Single iterable
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16]
print(type(map))
# Multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
summed = list(map(lambda x, y: x + y, a, b))
print(summed)  # [5, 7, 9]
from functools import reduce


product = reduce(lambda x, y: x * y, nums)
print(product)  # 24

# With initializer
product2 = reduce(lambda x, y: x * y, nums, 10)  # starts with 10
print(product2)  # 240


tp=enumerate(nums,0)
print(list(tp))