# flattenning a matrix (list of lists)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = []

# Using a for loop to flatten a matrix

for row in matrix:
    for item in row:
        flattened.append(item)

print(flattened)

# Using a list comprehension to flatten a matrix
flattenedC = [item for row in matrix for item in row]

print(flattenedC)