
#! AUTHOR :: RAHUL MISTRY
#! DATE   :: 09/04/2023

def print_fibo(n):
    # Print Fibo Series
    if n <= 0:
        return

    #define first and second element of fibo
    fibo1 = 0
    fibo2 = 1
    
    print(fibo1, end=" ")
    if n==1:
        return
    print(fibo2, end=" ")
    
    #Loop to print remaining numbers
    for i in range(2, n):
        fibo3 = fibo1 + fibo2
        print(fibo3, end=" ")
        fibo1 = fibo2
        fibo2 = fibo3

t = int(input())
for i in range(t):
    n = int(input())
    print_fibo(n)
    print()