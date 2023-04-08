
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 07/04/2023

T = int(input())

for i in range(T):
    side1, side2, side3 = map(int, input().split())
    if side1 + side2 >= side3 and side1 + side3 >= side2 and side2 + side3 >= side1:
        print(side1 + side2 + side3)
    else:
        print(-1)
