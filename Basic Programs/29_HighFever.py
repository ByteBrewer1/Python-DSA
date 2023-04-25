
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 09/04/2023

t = int(input())

high_temp = []
for _ in range(t):
    name, temp = input().split()
    temp = float(temp)
    if temp > 98.6:
        high_temp.append(name)
print(", ".join(high_temp))