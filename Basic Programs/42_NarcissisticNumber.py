# Write your code here
def is_armstrong_number(num):
    """Check if a number is an Armstrong number."""
    original_num = num
    sum_of_cubes = 0

    # Convert the number to a string to iterate over its digits
    num_str = str(num)
    num_len = len(num_str)

    # Calculate the sum of cubes of digits
    for digit in num_str:
        sum_of_cubes += int(digit) ** num_len

    # Check if the sum of cubes is equal to the original number
    if sum_of_cubes == original_num:
        return "Yes"
    else:
        return "No"


# Get the number of test cases
T = int(input())

# Process each test case
for i in range(T):
    num = int(input())
    result = is_armstrong_number(num)
    print(result)
