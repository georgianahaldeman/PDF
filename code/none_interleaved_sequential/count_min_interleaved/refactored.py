# Function to read numbers from the user
def read_numbers():
    input_string = input("Enter numbers separated by spaces: ")
    numbers_str = input_string.split()
    numbers = []
    for num_str in numbers_str:
        numbers.append(int(num_str))
    return numbers

# Function to find the minimum value in a list
def find_minimum(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

# Function to count how many times the minimum appears
def count_minimum(numbers, minimum):
    count = 0
    for num in numbers:
        if num == minimum:
            count += 1
    return count

# Main program
# numbers = read_numbers()
# minimum_value = find_minimum(numbers)
# minimum_count = count_minimum(numbers, minimum_value)

# print("The minimum value is:", minimum_value)
# print("It appears", minimum_count, "time(s) in the list.")