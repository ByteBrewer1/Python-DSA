
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 07/04/2023

T = int(input())

for _ in range(T):
    num = int(input())
    if(num == 7):
        print("EQUAL")
    elif(num > 7):
        print("UP")
    else:
        print("DOWN")
