
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

def digit_sum(number):
    number_str = str(number)
    sum = 0
    for digit in number_str:
        sum += int(digit)
    return sum

t = int(input())
for i in range(t):
    number = int(input())
    sum_digits = digit_sum(number)
    print(sum_digits)