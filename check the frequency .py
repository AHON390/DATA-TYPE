test = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 10
}

# Value to check frequency of
target_value = 10

# Count how many times the target value appears in the dictionary values
frequency = list(test.values()).count(target_value)

# Output the result
print(f"The value {target_value} appears {frequency} time(s) in the dictionary.")
