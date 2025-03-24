# Generator comphrehension

# Generator comprehension is similar to list comprehension but it uses () instead of []
# It is used to generate values on the fly and not store them in memory
# It is used to save memory

# sum of squares of numbers from 1 to 1,000,000

sum_of_squares = sum(x * x for x in range(1, 1_000_001))
print(sum_of_squares)