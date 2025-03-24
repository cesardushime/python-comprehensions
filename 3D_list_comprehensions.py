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

print(lst)

