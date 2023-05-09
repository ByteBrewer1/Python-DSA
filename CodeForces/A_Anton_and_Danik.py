import os
import re
import math
import random

n = int(input())
string = input().strip()
num_a = 0
num_d = 0

# Count the number of A and D in string
for c in string:
    if c == "A":
        num_a += 1
    elif c == "D":
        num_d += 1
# Determine the winner
if num_a > num_d:
    print("Anton")
elif num_a < num_d:
    print("Danik")
else:
    print("Friendship")
