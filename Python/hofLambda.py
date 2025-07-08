from functools import reduce

squared = lambda x: x*x

print(squared(5))

# when to use lambdas

def functionbuilder(y):
    return lambda x: x - y

subtract5 = functionbuilder(5)
print(subtract5(10))

# HOF: map

numbers = [1,2,3,4,5]

squared_numbers = map(lambda x: x*x, numbers)
print(list(squared_numbers))

# HOF: filter
odd_nums = filter(lambda x: x%2 != 0, numbers)
print(list(odd_nums))

# HOF: reduce
sum_of_nums = reduce(lambda acc,curr: acc + curr, numbers )
print(sum_of_nums)