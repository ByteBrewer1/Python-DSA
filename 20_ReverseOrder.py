
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 08/04/2023

n = int(input())

numbers = list(map(int, input().split()))

numbers.reverse()

print(*numbers)