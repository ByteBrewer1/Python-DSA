
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

def square_s(number):
    number_str = str(number)
    sum = 0
    for digit in number_str:
        square = int(digit) * int(digit)
        sum += int(square)
    return sum

t = int(input())
for i in range(t):
    number = int(input())
    square_sum = square_s(number)
    print(square_sum)