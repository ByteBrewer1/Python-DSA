import os
import math
import re

for _ in range(int(input())):
    money = int(input())
    # Round the money to nearest 10 multiple
    # if greater than 5 than increase
    # if less than or equal to 4 decrease
    if money % 10 == 0:
        print(100 - money)
    elif money % 10 < 5:
        print(100 - (money - money % 10))
    else:
        print(100 - (money + (10 - money % 10)))
