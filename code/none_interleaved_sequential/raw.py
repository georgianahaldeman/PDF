# Beginner-friendly Python code for the pseudocode

# Step 1: Read numbers from the user
input_string = input("Enter numbers separated by spaces: ")
numbers_str = input_string.split()  # Split the input into a list of strings
numbers = []                        # Empty list to store integers

# Convert each string to an integer
for num_str in numbers_str:
    numbers.append(int(num_str))

# Step 2: Assume the first number is the minimum
minimum = numbers[0]

# Step 3: Initialize the counter
counter = 0

# Step 4: Find the minimum and count its occurrences at the same time
for num in numbers:
    if num < minimum:
        minimum = num
        counter = 0  # Reset counter if a new minimum is found
    elif num == minimum:
        counter += 1  # Count the minimum

# Step 5: Display the result
print("The minimum value is:", minimum)
print("It appears", counter, "time(s) in the list.")
