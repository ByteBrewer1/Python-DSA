
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 07/04/2023

def print_digits(n):
    n_str = str(n)
    
    digit_1 = n_str[0]
    digit_2 = n_str[1]
    
    print(digit_1, digit_2, end=' ')

T = int(input())

for _ in range(T):
    n = int(input())
    print_digits(n)
    print()