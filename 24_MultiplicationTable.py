
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 07/04/2023

T = int(input())

for i in range(T):
    n = int(input())
    table = []
    for j in range(1,11):
        table.append(n * j)
    print(*table)
