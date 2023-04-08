
#! AUTHOR :: RAHUL MISTRY
#* DATE   :: 07/04/2023

T = int(input())

for i in range(T):
    temp, hum = map(int, input().split())
    if temp >= 30 and hum >= 90:
        print("Hot and Humid")
    if temp >= 30 and hum < 90:
        print("Hot")
    if temp < 30 and hum >= 90:
        print("Cool and Humid")
    if temp < 30 and hum < 90:
        print("Cool")

