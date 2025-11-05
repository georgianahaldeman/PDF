
# Step 1: Read numbers from the user
input_string = input("Enter numbers separated by spaces: ")
numbers_str = input_string.split()  # Split the input into a list of strings
numbers = []                        # Empty list to store integers

# Convert each string to an integer
for num_str in numbers_str:
    numbers.append(int(num_str))

# Step 2: Find the minimum value
minimum = numbers[0]  # Start by assuming the first number is the minimum
for num in numbers:
    if num < minimum:
        minimum = num

# Step 3: Count how many times the minimum appears
count = 0
for num in numbers:
    if num == minimum:
        count += 1

# Step 4: Show the result
print("The minimum value is:", minimum)
print("It appears", count, "time(s) in the list.")

