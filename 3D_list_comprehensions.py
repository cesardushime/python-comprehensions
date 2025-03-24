# Building a 3D list using list comprehensions

# Using a for loop to create a 3D list

lst = []
for i in range(3):
    inner1_lst = []
    for j in range(3):
        inner2_lst = []
        for k in range(3):
            inner2_lst.append(k)
        inner1_lst.append(inner2_lst)
    lst.append(inner1_lst)

# print(lst)

# Using a list comprehension to create a 3D list
mylist = [[[k for k in range(3)] for j in range(3)] for i in range(3)]

# flatten the 3D list
flattened = []

for inner1_lst in lst:
    for inner2_lst in inner1_lst:
        for item in inner2_lst:
            flattened.append(item)

# print(flattened)

# Using a list comprehension to flatten a 3D list
flaten = [item for inner1_lst in mylist for inner2_lst in inner1_lst for item in inner2_lst]
print(flaten)