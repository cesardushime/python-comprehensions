# Calling a function on a list comprehension

def square(x):
    return x**2

squared_numbers = [square(x) for x in range(11)]

print(squared_numbers)