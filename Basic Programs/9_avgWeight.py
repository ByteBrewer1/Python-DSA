# AUTHOR :: RAHUL MISTRY
# DATE   :: 07/04/2023

weights = list(map(float, input().split()))

n = len(weights)

avg = sum(weights) / n

print("{:.6f}".format(avg))