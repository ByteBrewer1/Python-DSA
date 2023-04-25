
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 07/04/2023

n = int(input())

digit1 = n // 100
digit2 = (n // 10) % 10
digit3 = n % 10

reverse_num = digit3 * 100 + digit2 * 10 + digit1
print(reverse_num)