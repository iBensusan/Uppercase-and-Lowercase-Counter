# Prompt the user to enter a sentence
text = input("Enter a sentence: ")

# Count uppercase letters using list comprehension
uppercase_count = sum(1 for char in text if char.isupper())
# Count lowercase letters using list comprehension
lowercase_count = sum(1 for char in text if char.islower())

# Display the results
print("The number of uppercase letters is:", uppercase_count)
print("The number of lowercase letters is:", lowercase_count)