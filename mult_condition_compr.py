# String that start with "a" and end in "y"

options = ["apple", "banana", "cherry", "apricot", "blueberry", "adajjdy", "ajldjy"]

valid_strings = []

# using for loop
for option in options:
    if len(option) <= 1:
        continue
    if option[0] != "a":
        continue
    if option[-1] != "y":
        continue
    valid_strings.append(option)



