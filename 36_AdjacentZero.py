
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

def has_zero(binaryNum):
    for i in range(len(binaryNum)-1):
        if binaryNum[i] == '0' and binaryNum[i+1] == '0':
            return True
    return False

t = int(input())

for i in range(t):
    binaryNum = input()
    if has_zero(binaryNum):
        print("Yes")
    else:
        print("No")