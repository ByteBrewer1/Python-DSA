
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

t = int(input())
for i in range(t):
    n = int(input())
    result = factorial(n)
    print(result)