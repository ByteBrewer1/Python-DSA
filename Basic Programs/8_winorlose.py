# AUTHOR :: RAHUL MISTRY
# DATE   :: 07/04/2023

n = int(input())

num = list(map(int, input().split()))

maxi = max(num)

if(maxi % 2):
    print("LOST")
else:
    print("WON")