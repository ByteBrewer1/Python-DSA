
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 07/04/2023

T = int(input())

for _ in range(T):
    temp = float(input())
    temp_f = ((9 * temp) / 5) + 32
    print("{:.2f}".format(temp_f))