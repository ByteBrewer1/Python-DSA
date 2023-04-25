
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

def isArmstrong(n):
    """Check if a number is an Armstrong number."""
    num_str = str(n)
    sum_cube = 0
    
    for digit in num_str:
        sum_cube += int(digit) ** 3
    
    if sum_cube == n:
        return "Yes"
    else:
        return "No"

t = int(input())
for i in range(t):
    n = int(input())
    result = isArmstrong(n)
    print(result)
