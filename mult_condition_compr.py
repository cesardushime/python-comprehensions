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

# using list comprehension
selected_string = [option for option in options if len(option) > 1 and option[0] == "a" and option[-1] == "y"]

print(f"Selected strings: {selected_string}")

