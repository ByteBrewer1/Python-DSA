# AUTHOR :: RAHUL MISTRY
# DATE   :: 04 / 06 / 2023

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    remaining_money = k
    result = ""
    for amount in arr:
        if amount <= remaining_money:
            result += '1'
            remaining_money -= amount
        else:
            result += '0'
    print(result)
