
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

def notDivisible(n):
    for i in range(1, n+1):
        if i % 3 != 0:
            print(i, end=" ")

T = int(input())

for _ in range(T):
    n = int(input())
    notDivisible(n)
    print()