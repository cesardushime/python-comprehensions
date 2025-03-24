# Generator comphrehension

# Generator comprehension is similar to list comprehension but it uses () instead of []
# It is used to generate values on the fly and not store them in memory
# It is used to save memory

# sum of squares of numbers from 1 to 10

sum_of_squares = sum(x**2 for x in range(1, 11))
print(sum_of_squares)