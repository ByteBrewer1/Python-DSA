
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

def sumProduct(n):
    digits = str(n)
    n_len = len(digits)
    _sum = 0
    _product = 1
    for digit in digits:
        _sum += int(digit)
        _product *= int(digit)
    if n == _sum * _product:
        return "Yes"
    else:
        return "No"
    
t = int(input())
for i in range(t):
    n = int(input())
    result = sumProduct(n)
    print(result)