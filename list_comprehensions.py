values = []
# Using a for loop to create a list of values
# for x in range(10):
#     values.append(x * 2)


# Using a list comprehension to create a list of values
values = [x * 2 for x in range(10)]
# print(values)

# Print all even and odd numbers separately from 0 to 50

even_numbers = [x for x in range(51) if x % 2 == 0]
odd_numbers = [x for x in range(51) if x % 2 != 0]
print(f"Even numbers:\n {even_numbers}")
print(f"Odd numbers:\n {odd_numbers}")

